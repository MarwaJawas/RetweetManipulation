#filter only retweet object and then store and insert data from json file into sqlite3
import sqlite3 as lite
import sys
import json
#from ast import literal_eval
#import time
#t1=time.time()
def insert_rt_jsonFile(json_file,database):
    try:
        con = lite.connect('%s.db'% (database) )
        cur = con.cursor()
        with open('%s.json' % (json_file) , 'r') as fh:
        
            for line in fh:
                if line.strip():
                    tweet_read=json.loads(line)
                
                    if "retweeted_status" in tweet_read.keys():
                    #print (tweet_read["user"]["id"])
            
                        #user object of retweeter
                
                        retweeter_id=tweet_read["user"]["id"]
                        secreen_name=tweet_read["user"]["screen_name"]
                        user_name=tweet_read["user"]["name"]
                        description=tweet_read["user"]["description"]
                        followers_count=tweet_read["user"]["followers_count"]
                        friends_count=tweet_read["user"]["friends_count"]
                        listed_count=tweet_read["user"]["listed_count"]
                        favourites_count=tweet_read["user"]["favourites_count"]
                        statuses_count=tweet_read["user"]["statuses_count"]
                        user_account_created_time=tweet_read["user"]["created_at"]
                        default_profile_image=tweet_read["user"]["default_profile_image"]
                    
                        
                        """
                        cur.execute('''
                      INSERT OR REPLACE INTO retweeter values (? , ?,?, ? ,? ,? ,? ,? ,? ,?,? )
                       ''',(retweeter_id,secreen_name,user_name ,description,followers_count,friends_count
                              ,listed_count,favourites_count,statuses_count
                              ,user_account_created_time,default_profile_image))
                        """
                       
                    
                        #tweet object
                        if "text" in tweet_read.keys():
                            tweet_text=tweet_read["retweeted_status"]["text"]
                    
                        else:
                            tweet_text=tweet_read["retweeted_status"]["full_text"]
                
                        tweet_id=tweet_read["retweeted_status"]["id"]
                        #tweet_text=tweet_read["retweeted_status"]["text"]
                        tweet_created_time=tweet_read["retweeted_status"]["created_at"]
                        tweet_source=tweet_read["retweeted_status"]["source"]
                        retweet_count=tweet_read["retweeted_status"]["retweet_count"]
                        favorite_count=tweet_read["retweeted_status"]["favorite_count"]
                    
                    
                        #user object of tweeter
                        tweeter_id=tweet_read["retweeted_status"]["user"]["id"]
                        tweeter_created_time=tweet_read["retweeted_status"]["user"]["created_at"]
                    
                        cur.execute("SELECT NOT EXISTS (SELECT 10 FROM tweet WHERE tweet_id=='%s'LIMIT 1)" % tweet_id) 
                        records = cur.fetchone()
                    
                        if records[0]==1:
                    
                            #URLs object inside tweet
                            tweet_urls=tweet_read["retweeted_status"]["entities"]["urls"]
                            if len (tweet_urls) > 0:
                                for tweet_url in tweet_urls:
                                    url=tweet_url["url"]    
                                    expanded_url=tweet_url["expanded_url"]
                                    display_url=tweet_url["display_url"]
                            
                                    cur.execute('''
                                      INSERT INTO URL  (tweet_id , url ,expanded_url,  display_url) values (?,?,?,?)
                                        ''' , (tweet_id, url, expanded_url, display_url ))        
                                    con.commit()
                    
                            #hashtags object inside tweet
                            tweet_hashtages=tweet_read["retweeted_status"]["entities"]["hashtags"]
                            if len (tweet_hashtages) > 0:
                                for tweet_hashtage in tweet_hashtages:
                                    text_hashtage=tweet_hashtage["text"]
                            
                                    cur.execute('''
                                      INSERT INTO hashtage (tweet_id , text_hashtage) values (?,?)
                                    ''' , (tweet_id, text_hashtage ))
                                    con.commit()
                    
                             #user_mentions object inside tweet
                            tweet_mentions=tweet_read["retweeted_status"]["entities"]["user_mentions"]
                            if len (tweet_mentions) > 0:
                                for tweet_mention in tweet_mentions:
                                    name_mention=tweet_mention["name"]
                                    screen_name_mention=tweet_mention["screen_name"]
                                    id_user_mention=tweet_mention["id"]
                            
                                    cur.execute('''
                                      INSERT INTO mention (tweet_id ,id_user_mention,name_mention ,screen_name_mention ) 
                                      values (?,?,?,?)
                                         ''' , (tweet_id, id_user_mention, name_mention, screen_name_mention ))
                                    con.commit()
                   
                        #retweet object
                        if "text" in tweet_read.keys():
                            retweet_text=tweet_read["text"]
                    
                        else:
                            retweet_text=tweet_read["full_text"]
                    
                        retweet_id=tweet_read["id"]
                        #retweet_text=tweet_read["text"]
                        retweet_created_time=tweet_read["created_at"]
                        #retweet_entities=tweet_read["entities"]
                        #retweet_extended_entities=tweet_read["extended_entities"]
                        
                        cur.execute('''
                          INSERT OR IGNORE INTO retweeter values (? , ?, ?, ? ,? ,? ,? ,? ,? , ?, ? )
                           ''',(retweeter_id,secreen_name,user_name ,description,followers_count,friends_count
                              ,listed_count,favourites_count,statuses_count
                              ,user_account_created_time,default_profile_image))
                        
                        cur.execute('''
                          INSERT OR IGNORE INTO tweet  values (?, ?, ?, ?,?,?)
                           ''',(tweet_id,tweet_text,tweet_created_time,tweet_source,retweet_count,favorite_count))
                    
                        cur.execute('''
                          INSERT OR IGNORE INTO tweeter  values (?, ?)
                          ''',(tweeter_id ,tweeter_created_time))
                    
                        cur.execute('''
                          INSERT  INTO retweet values (? ,?, ?, ?,?)
                         ''' , (retweet_id,retweet_text,retweet_created_time,tweet_id,retweeter_id ))
                   
                
                        con.commit()
            
                    else:
                        continue        
    
                else: 
                    continue
    except e:
        if con:
            con.rollback()
    
        print("Unexpected error %s:" % e.args[0])
        sys.exit(1)
    finally:
        if con:
            con.close()
        print("insert data from json file into database was done...")    
    return

#1) input json file name        
json_file = input("Enter json file name : ")
database = input("Enter database name : ")
#2) call function
insert_rt_jsonFile(json_file,database)        
        
