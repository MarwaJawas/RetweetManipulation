
import sqlite3 
import sys
import statistics as st




try:
    sqliteConnection = sqlite3.connect('Annual_bonus.db')
    cursor = sqliteConnection.cursor()
    #cursor.execute("SELECT NOT EXISTS (SELECT 400 FROM retweeter WHERE retweeter_id=2243086672 LIMIT 1)")
    
    #id=22430866723
    #cursor.execute("SELECT NOT EXISTS (SELECT 400 FROM retweeter WHERE retweeter_id=='%s'LIMIT 1)" % id)
    #records = cursor.fetchone()
    #print(records[0])
    
    #cursor.execute('''SELECT count (*) from
                   #(SELECT retweeter_id FROM retweet group by retweeter_id HAVING COUNT(* )>1)''')
    #records = cursor.fetchall()
    #print ("total retweeter have more than 1: ",records[0][0])
    q='''SELECT count (*) from retweeter'''
    for record in cursor.execute(q):
        if record!=None:
            print(record[0])
        #record = cursor.fetchone()
        #print(record)
        #if record!=None:
            #print(record)
    
    cursor.execute("SELECT count (*) FROM tweet")
    #cursor.execute('''SELECT count (*) FROM(SELECT tweet_id FROM retweet where retweeter_id IN
                   #(SELECT retweeter_id FROM retweet group by retweeter_id HAVING COUNT(* )>1))''')
         
    records = cursor.fetchall()
    print ("total tweet: ",records[0][0])
    
    cursor.execute("SELECT count (*) FROM retweet")
    records = cursor.fetchall()
    print ("total retweet: ",records[0][0])
                   
    cursor.execute("SELECT count (*) FROM retweeter")
    records = cursor.fetchall()
    print ("total retweeter: ",records[0][0])
    #cursor.execute("SELECT retweeter_id FROM retweet group by retweeter_id HAVING COUNT(* )>2")
    cursor.execute('''SELECT count (*) FROM 
                   ( SELECT retweeter_id, count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>2)''')
    records = cursor.fetchall()
    print ("retweeters have retweeted more than 2  : ",records[0][0])
    
    cursor.execute('''SELECT count (*) FROM 
                   ( SELECT retweeter_id, count (*) FROM retweet group by retweeter_id HAVING COUNT(* )==1)''')
    records = cursor.fetchall()
    print ("retweeters have retweeted one tweet  : ",records[0][0])
    
    cursor.execute('''SELECT count (*) FROM 
                   ( SELECT retweeter_id, count (*) FROM retweet group by retweeter_id HAVING COUNT(* )==2)''')
    records = cursor.fetchall()
    print ("retweeters have retweeted two tweet  : ",records[0][0])
    
    cursor.execute('''SELECT count (*) FROM 
                   ( SELECT retweeter_id, count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>4)''')
    records = cursor.fetchall()
    print ("retweeters have retweeted more than 4 tweet  : ",records[0][0])
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    #print (" number of retweet   : ",records)
    
    ferquency_retweets_for_retweeters=[item[0] for item in records]
    #print(rtweets)
    median_value= st.median(ferquency_retweets_for_retweeters)
    print("median value of ferquency of retweets:  " , median_value)
    
    cursor.execute("SELECT count (*) FROM ( SELECT retweeter_id, count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>2)")
    records = cursor.fetchall()
    print ("retweeters have retweeted more than 2  : ",records[0][0])
    
    
    #cursor.execute("SELECT retweeter_id , count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>40")
    #records = cursor.fetchall()
    #print ("retweeters have retweeted more than 40  : ",sorted (records))
    """
    for record in cursor.execute("SELECT retweeter_id , count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>40"):
        if record!=None:
            print("retweeter_id:  ",record[0],"count retweet:  ",record[1])
    """
    """
    # function to return the second element of the 
    # two elements passed as the parameter 
    def sortSecond(val): 
        return val[1]

    cursor.execute("SELECT retweeter_id , count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>40")
    records = cursor.fetchall()
    records.sort(key = sortSecond , reverse = True)
    for r in records:
        print("retweeter_id:  ",r[0],"count retweet:  ",r[1])
    """ 
    
    cursor.execute('''SELECT count (*) FROM 
                   ( SELECT retweeter_id, count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>19)''')
    
    records = cursor.fetchall()
    print ("retweeters have retweeted more than 19  : ",records[0][0])
    
    cursor.execute('''SELECT retweeter_id, tweet_id FROM retweet where retweeter_id IN
                   (SELECT retweeter_id FROM retweet group by retweeter_id HAVING COUNT(* )>40)''')
    records = cursor.fetchall()
    #rtweeters_id_tweet=[item[0] for item in records]
    print ("retweeters id & tweet id have retweeted more than 40  : ",len(records))
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    
    print ("average value ferquency of retweets   : " ,records[0][0])
    
    cursor.execute('''SELECT count_retweet FROM 
                       ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>40) 
                               ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    #print (" number of retweet   : ",records)
    
    rtweets=[item[0] for item in records]
    #print(rtweets)
    median_value= st.median(rtweets)
    #print("median_value of retweeter more than 40:  " , median_value)
    
    
    
    """
    cursor.execute("SELECT count_retweet FROM 
    ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>40) ORDER BY count_retweet LIMIT 1 OFFSET (( SELECT count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>40) -1 )/2 ")
    records = cursor.fetchall()
    print (" number of retweet   : ",records)
    #SELECT x FROM MyTable ORDER BY x LIMIT 1 OFFSET (SELECT COUNT(*) FROM MyTable) / 2
    """
    """
    cursor.execute("SELECT retweeter_id, count (*) FROM retweet group by retweeter_id HAVING COUNT(* )>40")
    records = cursor.fetchall()
    print ("retweeters have retweeted more that 2  : ",records)   
    """       

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
4408
total tweet:  2073
total retweet:  10191
total retweeter:  4408
retweeters have retweeted more than 2  :  809
retweeters have retweeted one tweet  :  3024
retweeters have retweeted two tweet  :  575
retweeters have retweeted more than 4 tweet  :  397
median value of ferquency of retweets:   1.0
retweeters have retweeted more than 2  :  809
retweeters have retweeted more than 19  :  42
retweeters id & tweet id have retweeted more than 40  :  1214
average value ferquency of retweets   :  2.3119328493647915
The SQLite connection is closed
#compute total number of retweeter , median ,and average value of ferquency of retweets
import sqlite3 
import sys
import statistics as st


try:
    sqliteConnection = sqlite3.connect('amar_malki.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute("SELECT count (*) FROM retweet")
    records = cursor.fetchall()
    print ("total retweet: ",records[0][0])
                   
    cursor.execute("SELECT count (*) FROM retweeter")
    records = cursor.fetchall()
    print ("total retweeter: ",records[0][0])
    
    cursor.execute("SELECT count (*) FROM ( SELECT retweeter_id  FROM retweet group by retweeter_id HAVING COUNT(* )>1)")
    records = cursor.fetchall()
    print (" retweeter more that 1 retweet: ",records[0][0])
    
    cursor.execute('''SELECT count_retweet FROM 
                ( SELECT  count (*) as count_retweet FROM retweet group by retweeter_id HAVING COUNT(* )>0)
                   ORDER BY count_retweet  ''')
    records = cursor.fetchall()
    
    ferquency_retweets_for_retweeters=[item[0] for item in records]
    
    median_value= st.median(ferquency_retweets_for_retweeters)
    print("median value of ferquency of retweets:  " , median_value) 
    
    cursor.execute('''SELECT avg(count_retweet) FROM 
                                              ( SELECT  count (*) as count_retweet 
                                               FROM retweet group by retweeter_id HAVING COUNT(* )>0)''')
    records = cursor.fetchall()
    print ("average value ferquency of retweets   : ",records[0][0])    

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
total retweet:  61961
total retweeter:  39392
 retweeter more that 1 retweet:  9093
median value of ferquency of retweets:   1.0
average value ferquency of retweets   :  1.572933590576767
The SQLite connection is closed
# identify outliers with interquartile range

import numpy as np
#from numpy import percentile
# seed the random number generator
#seed(1)
# generate univariate observations
#data = 5 * randn(10000) + 50

data=ferquency_retweets_for_retweeters
#dataset=sorted(data)
# calculate interquartile range
#q1, q3= percentile(dataset,[25,75])
#iqr = q3 - q1
q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
iqr = q75 - q25
#print('Percentiles: 25th=%.3f, 75th=%.3f, IQR=%.3f' % (q25, q75, iqr))
#print('Percentiles: 25th=%s , 75th=%s , IQR=%s' % (q1, q3, iqr))
print('Percentiles: 25th=%s , 75th=%s , IQR=%s' % (q25, q75, iqr))
# calculate the outlier cutoff
cut_off = iqr * 1.5
lower, upper = q25 - cut_off, q75 + cut_off
print('lower limit =%s , upper limit =%s' %(lower, upper))
# identify outliers
outliers = [x for x in data if x < lower or x > upper]
#print('outliers values (outliers retweeters): %s' % outliers)
print('Identified outliers (outliers retweeters): %d' % len(outliers))
# remove outliers
outliers_removed = [x for x in data if x >= lower and x <= upper]
print('Non-outlier observations (normal retweeters): %d' % len(outliers_removed))
Percentiles: 25th=1.0 , 75th=3.0 , IQR=2.0
lower limit =-2.0 , upper limit =6.0
Identified outliers (outliers retweeters): 7160
Non-outlier observations (normal retweeters): 54578
import numpy as np
import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots( figsize=(9, 9))
ax1.set_title('boxplot: frequency of retweets for each retweeter ')
#green_diamond = dict(markerfacecolor='g', marker='D')
green_diamond = dict(markerfacecolor='r')
ax1.boxplot(ferquency_retweets_for_retweeters,flierprops=green_diamond )
ax1.yaxis.grid(True)
#ax1.set_yticks([y for y in range(len(ferquency_retweets_for_retweeters))])
#ax1.set_xlabel('retweeter id')
ax1.set_ylabel('retweeting frequency ')
plt.savefig('boxplot_hashtage_alhilal.png', dpi=800)
#mean and standaur divation
#from numpy.random import seed
#from numpy.random import randn
from numpy import mean
from numpy import std
# seed the random number generator
#seed(1)
# generate univariate observations
#data = 5 * randn(10000) + 50
# calculate summary statistics
data_mean, data_std = mean(ferquency_retweets_for_retweeters), std(ferquency_retweets_for_retweeters)
print("data_mean=%.3f , data_std=%.3f "% (data_mean, data_std))
# identify outliers
cut_off = data_std * 3
lower, upper = data_mean - cut_off, data_mean + cut_off
# identify outliers
outliers = [x for x in data if x < lower or x > upper]
print('Identified outliers: %d' % len(outliers))
print('Identified outliers: %s' % outliers)
# remove outliers
#outliers_removed = [x for x in data if x >= lower and x <= upper]
print('Non-outlier observations: %d' % len(outliers_removed))
data_mean=3.104 , data_std=4.965 

import numpy as np
import pandas as pd
outliers=[]
def detect_outlier(data_1):
    
    threshold=3
    mean_1 = np.mean(data_1)
    std_1 =np.std(data_1)
    
    
    for y in data_1:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers

outlier_datapoints = detect_outlier(ferquency_retweets_for_retweeters)
print(len(outlier_datapoints))
print(outlier_datapoints)

import sqlite3 
import sys
#for network creation


try:
    sqliteConnection = sqlite3.connect('Retweet_manipulation.db')
    cursor = sqliteConnection.cursor()
    
    #cursor.execute("SELECT retweeter_id FROM retweet group by retweeter_id HAVING  COUNT(retweet_id )>70")
    cursor.execute("SELECT retweet_id FROM retweet where retweeter_id ='%s'" % 1101078926745583616)    
    set_tweet_of_useri=[row[0] for row in cursor.fetchall()]
    #print (set_tweet_of_useri)
    print(len(set_tweet_of_useri))
    
    #cursor.execute("SELECT retweeter_id FROM retweeter")
    #records_retweeter = cursor.fetchall()    
    #set_retweeter=[row[0] for row in records]
    #print (len (records_retweeter))
    #for retweetier in records_retweeter:
        #print (retweetier)
except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
import sqlite3 
import sys
import statistics as st


try:
    sqliteConnection = sqlite3.connect('third_World_War.db')
    cursor = sqliteConnection.cursor()
    
    cursor.execute("SELECT count(*) from (SELECT retweet_id FROM retweet where retweeter_id='%s') " % 454678027)
    records = cursor.fetchall()
    for r in records:
        print (r)
        
    cursor.execute("SELECT url,expanded_url,display_url FROM URL where tweet_id='%s' " % 1192945793768013824)
    records = cursor.fetchall()
    for r in records:
        print (r)
        
    cursor.execute("SELECT screen_name_mention FROM mention where tweet_id='%s' " % 1192945793768013824)
    records = cursor.fetchall()
    for r in records:
        print (r)    
     

    cursor.close()

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
(10,)
The SQLite connection is closed
891899698411425792
import sqlite3 
import sys
import statistics as st




try:
    sqliteConnection = sqlite3.connect('Saudi_Qatar.db')
    cursor = sqliteConnection.cursor()
    #cursor.execute("SELECT NOT EXISTS (SELECT 400 FROM retweeter WHERE retweeter_id=2243086672 LIMIT 1)")
    
    #id=22430866723
    #cursor.execute("SELECT NOT EXISTS (SELECT 400 FROM retweeter WHERE retweeter_id=='%s'LIMIT 1)" % id)
    #records = cursor.fetchone()
    #print(records[0])
    
    #cursor.execute('''SELECT count (*) from
                   #(SELECT retweeter_id FROM retweet group by retweeter_id HAVING COUNT(* )>1)''')
    #records = cursor.fetchall()
    #print ("total retweeter have more than 1: ",records[0][0])
    #q='''SELECT secreen_name from retweeter where retweeter_id=605037339'''
    #q=''' SELECT  count (*) FROM retweet where retweeter_id=605037339 '''
    q='''SELECT secreen_name FROM retweeter where retweeter_id IN
                   ( SELECT retweeter_id FROM retweet group by retweeter_id HAVING COUNT(* )=89)'''
    for record in cursor.execute(q):
        if record!=None:
            print(record[0])
        #record = cursor.fetchone()
        #print(record)
        #if record!=None:
            #print(record)
    
    
   

except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
Bitchdel99
lanetamexfood
renunciasenador
priissilva14
daytrigo
1Dforever1239
YohnniAlex
AngelaLeivaROS
alcobaaeric
The SQLite connection is closed
import json
import sqlite3 
import sys
with open('rtg_hashtag_alhilal.json','r') as reader:
        
    for line in reader:
        #skip empty line
        if line.strip():
            
            retweeter_group_read=json.loads(line)
            group_id=retweeter_group_read["group_id"]
            members_id=retweeter_group_read["members_id"]
            if group_id=="64b483729e994b7e99c016be60cdc6e0":
            #if group_id=="5ca0e9316448405785e348cc30002dc0":
                sqliteConnection = sqlite3.connect("Retweet_manipulation3.db")
                cursor = sqliteConnection.cursor()
    
                tuple_set_retweeter=tuple(members_id)
    #print(tuple_set_retweeter)
    
                cursor.execute("SELECT retweet_count from tweet where tweet_id IN (select tweet_id FROM retweet WHERE retweeter_id IN %s)" % (tuple_set_retweeter,))
                retweet_count= cursor.fetchall()
                set_tweet=[]
                set_tweet=[row[0] for row in retweet_count]
                print(set_tweet)
                print(len(set_tweet))
                #create_graph(group_id,members_id ,'hashtag_abdulaziz.db')
                print("\n")
                print("\n")
                print("\n")
                
        else:
            continue
            







from collections import Counter
#l = [1, 1, 2, 2, 2, 2, 2, 3, 4, 10, 10, 10, 10, 10]
c = Counter(set_tweet)
[(i, c[i] / len(set_tweet) * 100.0) for i in c]
[(9, 74.4186046511628), (10, 25.581395348837212)]
 