import networkx as nx

import sqlite3 

import pandas as pd
import numpy as np
import math

import json
from collections import Counter
from itertools import combinations
import re
import dateutil.parser
import datetime
import statistics as st

"""
from scipy.stats import entropy
data=[]
pd_series = pd.Series(data)
counts = pd_series.value_counts()
entropy = entropy(counts, base=2)
"""
#entropy
def entropy(list_of_elements):
    if not list_of_elements:
        #print "list empty"
        return -1
    entropy = 0
    total_elements = len(list_of_elements)
    c=Counter(list_of_elements)
    input_dict = dict(c)
    for key, value in input_dict.items():
        p = float(value)/total_elements
        p_ = float(1)/p
        log2_p = math.log(p_, 2)
        ent = p*log2_p
        entropy+=ent
    return entropy

def graph_features(retweeter_graph ,members_id):

    #avg_neighbor_degree = nx.average_neighbor_degree(retweeter_graph, weight='weight')
    avg_neighbor_degree =  nx.average_neighbor_degree(retweeter_graph,nodes=members_id, weight='weight')
    avg_neighbor_degree_entropy = entropy(avg_neighbor_degree.values())
    avg_neighbor_degree_sd= st.pstdev(avg_neighbor_degree.values())
    avg_neighbor_degree_mean = st.mean(avg_neighbor_degree.values())
    #print(m_ean)
    #cov = s_dev/float(m_ean)
    if avg_neighbor_degree_mean!=0:
        avg_neighbor_degree_cov = avg_neighbor_degree_sd/avg_neighbor_degree_mean
    else:
        avg_neighbor_degree_cov=0
    
    #print(avg_neighbor_degree_entropy )
    #print(members_id)

    avg_degree_connectivity = nx.average_degree_connectivity(retweeter_graph,nodes=members_id,weight='weight')
    avg_degree_connectivity_entropy = entropy(avg_degree_connectivity.values())
    avg_degree_connectivity_sd= st.pstdev(avg_degree_connectivity.values())
    avg_degree_connectivity_mean = st.mean(avg_degree_connectivity.values())
    if avg_degree_connectivity_mean!=0:
        avg_degree_connectivity_cov = avg_degree_connectivity_sd/avg_degree_connectivity_mean
    else:
        avg_degree_connectivity_cov=0
    
    #eccent = nx.eccentricity(retweeter_graph,v=members_id)
    #eccentricity_entropy = entropy(eccent.values())
    #print(eccent.values())
    #print(list(retweeter_graph.degree(weight='weight')))
    return  avg_neighbor_degree_entropy, avg_neighbor_degree_sd, avg_neighbor_degree_mean,avg_neighbor_degree_cov, avg_degree_connectivity_entropy,avg_degree_connectivity_sd,avg_degree_connectivity_mean,avg_degree_connectivity_cov

##temporal features

def gridCalculation(pairsGroupWise_x, pairsGroupWise_y, lengthOfGroup):
    # Square grid calculations
    xVals = np.array(pairsGroupWise_x)
    yVals = np.array(pairsGroupWise_y)

    grid = 0

    gridx = np.linspace(0, lengthOfGroup, lengthOfGroup)
    gridy = np.linspace(0, lengthOfGroup, lengthOfGroup)

    #print len(gridx)
    #print len(gridy)


    if len(gridx) < 2:
        grid = 0

    elif len(gridy) < 2:
        grid = 0

    else:
        grid,_,_ = np.histogram2d(xVals, yVals, bins=[gridx, gridy])
    return grid

def density_features(created_time_arr):
    postingTime_sorted = sorted(created_time_arr)
    deltaArr = []
    for c, value in enumerate(postingTime_sorted):

        if c == len(postingTime_sorted)-1:
            break
        deltaArr.append((postingTime_sorted[c+1] - value).total_seconds())

    for (p, item) in enumerate(deltaArr):
        if item < 1:
            deltaArr[p] = 2

    pairsOfDelta_x = []
    pairsOfDelta_y = []
    pairsGroupWise_x = []
    pairsGroupWise_y = []

    for i in range(len(deltaArr) - 1):
        current_item, next_item = deltaArr[i], deltaArr[i + 1]
        pairsOfDelta_x.append(math.log(current_item))
        pairsOfDelta_y.append(math.log(next_item))


    pairsGroupWise_x.extend(pairsOfDelta_x)
    pairsGroupWise_y.extend(pairsOfDelta_y)

    pairsGroupWise_x = [int(i) for i in pairsGroupWise_x]
    pairsGroupWise_y = [int(i) for i in pairsGroupWise_y]


    min_x, max_x = min(pairsGroupWise_x), max(pairsGroupWise_x)
    min_y, max_y = min(pairsGroupWise_y), max(pairsGroupWise_y)
    m = max(max_x - min_x + 1, max_y - min_y + 1)

    #density_grid = np.zeros(5)

    density_grid = gridCalculation(pairsGroupWise_x, pairsGroupWise_y, m)


    if type(density_grid) is np.ndarray:
        density = (density_grid.max()/sum(map(sum,density_grid)))
    else:
        density = 0

    return density

def retweeting_time_dispersion(all_members_arr):
    #print(all_members_arr)
    all_std_arr = []
    all_diff_arr = []
    for a_list in all_members_arr:
        sorted_list = sorted(a_list)
        diff_arr = []

        for c, value in enumerate(sorted_list):
            if c == len(sorted_list)-1:
                break
            diff_arr.append((sorted_list[c+1] - value).total_seconds())
        all_diff_arr.append(diff_arr)

    #print(all_diff_arr)
    for diff in all_diff_arr:
        all_std_arr.append(st.pstdev(diff))

    #print(all_std_arr)
    s_dev = st.pstdev(all_std_arr)
    #print(s_dev)
    m_ean = st.mean(all_std_arr)
    #print(m_ean)
    #cov = s_dev/float(m_ean)
    if m_ean!=0:
        cov = s_dev/m_ean
    else:
        cov=0
    return s_dev, m_ean, cov

def creation_time_dispersion(rt_user_created_time_arr):
    t_diff_list = []
    sorted_time_list = sorted(rt_user_created_time_arr)
    for c, value in enumerate(sorted_time_list):
        if c == len(sorted_time_list)-1:
            break
        t_diff_list.append((sorted_time_list[c + 1] - value).total_seconds())

    sde_v = st.pstdev(t_diff_list)
    mea_n = st.mean(t_diff_list)
   
    #cov = sde_v/float(mea_n)
    cov = sde_v/mea_n
    return sde_v, mea_n, cov


def temporal_features(group_id,list_retweeters,name_db):
    sqliteConnection = sqlite3.connect(name_db)
    cursor = sqliteConnection.cursor()
    
    #group, total_count = args
    #user_id = group['group_ids']
    #label = group['label']
    #sn = group['sn']
    retweeter_created_time_list = []

    source_tweet_created_time_arr = []
    source_user_created_time_arr = []
    all_user_rt_tt_diff = []
    rt_tweet_created_time_arr = []
    #rt_user_created_time_arr = []
    all_members_rting_arr = []

    for retweeter in list_retweeters:
        single_member_rting_arr = []
        single_user_rt_tt_diff = []
        
        cursor.execute('''SELECT created_time FROM retweeter WHERE retweeter_id ='%s' ''' %  retweeter )
        retweeter_created_time = cursor.fetchone()
        retweeter_created_time_list.append(datetime.datetime.strptime(dateutil.parser.parse(retweeter_created_time[0]).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S'))
        
        cursor.execute('''SELECT created_time FROM retweet WHERE retweet_id IN 
                      (SELECT retweet_id FROM retweet WHERE retweeter_id ='%s' ''' %  retweeter + ')' )
        """
        retweet_created_time = cursor.fetchall()
        for rt_time in retweet_created_time:
            single_member_rting_arr.append(datetime.datetime.strptime(dateutil.parser.parse(rt_time[0]).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S'))
        """
        while True:
            retweet_created_time = cursor.fetchone()
            
            
            if retweet_created_time==None:
                break
            single_member_rting_arr.append(datetime.datetime.strptime(dateutil.parser.parse(retweet_created_time[0]).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S'))
            
        all_members_rting_arr.append(single_member_rting_arr)
        
        
        cursor.execute('''SELECT retweet.created_time ,tweet.created_time FROM retweet INNER JOIN tweet 
                       on tweet.tweet_id = retweet.tweet_id
                       WHERE retweet.retweet_id IN 
                      (SELECT retweet_id FROM retweet WHERE retweeter_id ='%s' ''' %  retweeter + ')' )
        
        while True:
            rt_tt_created_time = cursor.fetchone()
            
            if rt_tt_created_time==None:
                break
        
            rt = datetime.datetime.strptime(dateutil.parser.parse(rt_tt_created_time[0]).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
            rt_tweet_created_time_arr.append(rt)
            #single_member_rting_arr.append(datetime.datetime.strptime(dateutil.parser.parse(d['rt_tweet_created_time']).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S'))
            tt = datetime.datetime.strptime(dateutil.parser.parse(rt_tt_created_time[1]).strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
            single_user_rt_tt_diff.append((rt - tt).total_seconds())
            
            
        all_user_rt_tt_diff.append(st.median(single_user_rt_tt_diff))
    #print(all_members_rting_arr)    
    ipt_d = density_features(rt_tweet_created_time_arr)
    rter_creation_d_std, rter_creation_mean, rter_creation_d_cov = creation_time_dispersion(retweeter_created_time_list)
    s_td, me_an, co_v = retweeting_time_dispersion(all_members_rting_arr)

    cov_of_response_times = st.pstdev(all_user_rt_tt_diff)/float(st.mean(all_user_rt_tt_diff))
    return group_id, ipt_d, s_td, me_an, co_v, cov_of_response_times, rter_creation_d_std, rter_creation_mean, rter_creation_d_cov 

##rt_tw features
def digitsInScreenName(screen_name):
    numbers = sum(c.isdigit() for c in screen_name)
    return numbers

def hashtagsInUserName(user_name):
    hashtags = {tag.strip("#") for tag in user_name.split() if tag.startswith("#")}
    if hashtags:
        return len(hashtags)
    return 0

#white-space detect
def detectSpecialCharacters(name):
    specialcharsInnames = re.sub('[\w]+' ,'', name)
    # Length of special characters of usernames and screenames
    return len(specialcharsInnames)

def getUrlMentionsHashtags(string):
    if string == None:
        return 0,0,0
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    mentions = re.findall('(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)',string)
    hashtags = re.findall('#(\w+)', string)

    return len(urls), len(mentions), len(hashtags)

def retweeter_tweet_features(label,list_retweeters,name_db):
    sqliteConnection = sqlite3.connect(name_db)
    cursor = sqliteConnection.cursor()
   
    #tuple_set_retweeter=tuple(list_retweeters)
    #print(tuple_set_retweeter)
    #group, total_count = args
    #user_id = group['pruned_group']
    #label = group['label']
    #sn = group['sn']
    #print sn
    
    digitsInScreenName_list = []
    hashtagsInUserName_list = []
    specialCharacters_sname_list = []
    specialCharacters_uname_list = []
    url_in_bio_list = []
    mention_in_bio_list = []
    hashtags_in_bio_list = []
    length_screen_name_list = []
    length_user_name_list = []
    rt_user_statuses_count_list = []
    rt_user_listed_count_list = []
    rt_user_favourites_count_list = []
    

    for retweeter in list_retweeters:
        #print(retweeter )
        #retweeter_id=tuple(retweeter_id)
        
    
        cursor.execute('''SELECT secreen_name,user_name,description,listed_count,favourites_count,statuses_count
                       FROM retweeter WHERE retweeter_id ='%s' ''' %  retweeter)
        retweeter_record = cursor.fetchone()
        #retweeter_record = cursor.fetchall()
        #set_tweet=[]
        #set_tweet=[row[1] for row in retweeter_tweet_ids_records]
        """
        
        ,(retweeter_id,secreen_name,user_name ,description,followers_count,friends_count
                              ,listed_count,favourites_count,statuses_count
                              ,user_account_created_time,default_profile_image))
        retweeter_id=row[0]                      
        """ 
        
        
        digitsInScreenName_list.append(digitsInScreenName(retweeter_record[0]))
        hashtagsInUserName_list.append(hashtagsInUserName(retweeter_record[1]))
        #specialCharacters_sname_list.append(detectSpecialCharacters(retweeter_record[0]))
        specialCharacters_uname_list.append(detectSpecialCharacters(retweeter_record[1]))
        ul,ms,hs = getUrlMentionsHashtags(retweeter_record[2])
        url_in_bio_list.append(ul)
        mention_in_bio_list.append(ms)
        hashtags_in_bio_list.append(hs)
        length_screen_name_list.append(len(retweeter_record[0]))
        length_user_name_list.append(len(retweeter_record[1]))
        rt_user_listed_count_list.append(retweeter_record[3])
        rt_user_favourites_count_list.append(retweeter_record[4])
        rt_user_statuses_count_list.append(retweeter_record[5])
        
        
            
            
   
        #rter = db[collectionName].find({'rt_user_id': user}).limit(1)
        #for i in rter:
            


    digitsInScreenName_entropy = entropy(digitsInScreenName_list)

    hashtagsInUserName_entropy = entropy(hashtagsInUserName_list)

    #specialCharacters_sname_entropy = entropy(specialCharacters_sname_list)

    specialCharacters_uname_entropy = entropy(specialCharacters_uname_list)

    url_in_bio_entropy = entropy(url_in_bio_list)

    mention_in_bio_entropy = entropy(mention_in_bio_list)

    hashtags_in_bio_entropy = entropy(hashtags_in_bio_list)

    length_screen_name_entropy = entropy(length_screen_name_list)

    length_user_name_entropy = entropy(length_user_name_list)

    rt_user_statuses_count_entropy = entropy(rt_user_statuses_count_list)

    rt_user_listed_count_entropy = entropy(rt_user_listed_count_list)

    rt_user_favourites_count_entropy = entropy(rt_user_favourites_count_list)
    
    stdev_statuses_count = st.pstdev(rt_user_statuses_count_list)
    stdev_listed_count = st.pstdev(rt_user_listed_count_list)
    stdev_favourites_count = st.pstdev(rt_user_favourites_count_list)
    #"SELECT retweeter_id, tweet_id FROM retweet WHERE retweeter_id IN %s" % (tuple_set_retweeter,)
    tuple_set_retweeter=tuple(list_retweeters)
    cursor.execute('''SELECT expanded_url FROM URL WHERE tweet_id IN
                       (SELECT tweet_id FROM retweet where retweeter_id IN  %s) ''' %  (tuple_set_retweeter,)
                       )
    url_record = cursor.fetchall()
    url_in_tweet_list=[url[0] for url in url_record]
  
    url_in_tweet_list_entropy =entropy(url_in_tweet_list)
   
    cursor.execute('''SELECT id_user_mention FROM mention WHERE tweet_id IN
                       (SELECT tweet_id FROM retweet where retweeter_id IN %s ) ''' %  (tuple_set_retweeter,)
                       )
    mention_record = cursor.fetchall()
    mention_in_tweet_list=[mention[0] for mention in mention_record]
    
    mention_in_tweet_list_entropy =entropy(mention_in_tweet_list)
    
    
    
    
    return  digitsInScreenName_entropy, hashtagsInUserName_entropy,specialCharacters_uname_entropy,url_in_bio_entropy, mention_in_bio_entropy, hashtags_in_bio_entropy, length_screen_name_entropy,length_user_name_entropy,rt_user_statuses_count_entropy, rt_user_listed_count_entropy, rt_user_favourites_count_entropy, stdev_statuses_count, stdev_listed_count , stdev_favourites_count,url_in_tweet_list_entropy,mention_in_tweet_list_entropy , label


###########################
G=nx.read_weighted_edgelist("amar_malki.weighted.edgelist")
all_result_features=[]
#read json file 
name_database='amar_malki.db'
with open('rtg_amar_malki.json','r') as reader:
        
    for line in reader:
        #skip empty line
        if line.strip():
            
            retweeter_group_read=json.loads(line)
            
            group_id=retweeter_group_read["group_id"]
            label=retweeter_group_read["label"]
            members_id=retweeter_group_read["members_id"]
            
            """
            temporal_features=temporal_features(group_id,members_id,name_database)
            
            member_str=[str(i) for i in members_id]
            graph_features=graph_features(G,member_str)
            
            rt_tw_features=retweeter_tweet_features(label,members_id,name_database)
            
            all_features=temporal_features + graph_features+rt_tw_features
            """
            member_str=[str(i) for i in members_id]
            all_features=temporal_features(group_id,members_id,name_database)+graph_features(G,member_str)+retweeter_tweet_features(label,members_id,name_database)
            all_result_features.append(all_features)
            print("group id: ",group_id," was finished..")
                
        else:
              continue
                


            
                
df3 = pd.DataFrame(all_result_features, columns=['groupID', 'inter_posting_time_compactness', 'retweeting_time_distribution_sd',
'retweeting_time_distribution_mean', 'retweeting_time_distribution_cov', 'cov_response_time',
'user_creation_time_distribution_sd', 'user_creation_time_distribution_mean', 'user_creation_time_distribution_cov', 'avg_neighbor_degree_entropy', 'avg_neighbor_degree_sd', 'avg_neighbor_degree_mean','avg_neighbor_degree_cov','avg_degree_connectivity_entropy', 'avg_degree_connectivity_sd','avg_degree_connectivity_mean','avg_degree_connectivity_cov','digitsInScreenName_entropy', 'hashtagsInUserName_entropy',
         'specialCharacters_uname_entropy', 'url_in_bio_entropy',
        'mention_in_bio_entropy', 'hashtags_in_bio_entropy', 'length_screen_name_entropy','length_user_name_entropy',
    'statuses_count_entropy', 'listed_count_entropy', 'favourites_count_entropy','standard_dev_statuses_count', 'standard_dev_listed_count' , 'standard_dev_favourites_count','url_in_tweet_list_entropy','mention_in_tweet_list_entropy','label'])

                                                 
 


df3.to_csv('extracted_amar_malki_feat.csv', sep=',', encoding='utf-8',index=False)




