#store and insert data from json file into sqlite3
import sqlite3 as lite
import sys
import json
from ast import literal_eval
read=0
try:
    
    with open('Rest_retweet_20191201-224549.json','r') as fh:
        
        for line in fh:
            
            tweet_read=json.loads(line)
            read+=1
                
            if "retweeted_status" in tweet_read.keys():
            #print (tweet_read["user"]["id"])
            
              
                
                #retweet object
                retweet_created_time=tweet_read["created_at"]
                #retweet_id=tweet_read["id"]
                
                if "text" in tweet_read.keys():
                    retweet_text=tweet_read["text"]
                    print("one retweet:   ")
                    print(retweet_text)
                else:
                    retweet_text=tweet_read["full_text"]
                    #print("one retweet:   ")
                    #print(retweet_text)
                    
                #retweet_created_time=tweet_read["created_at"]
                #retweet_entities=tweet_read["entities"]
                #retweet_extended_entities=tweet_read["extended_entities"]
                retweet_entities=tweet_read["entities"]
                
                """
                if "urls" in retweet_entities.keys():
                    retweet_urls=tweet_read["entities"]["urls"]
                    #print(urls)
                    
                    if len (retweet_urls) > 0:
                        for retweet_url in retweet_urls:
                            url=retweet_url["url"]
                            expanded_url=retweet_url["expanded_url"]
                            display_url=retweet_url["display_url"]
                            print("url of retweet:   ")
                            print(url)
                            print(expanded_url)
                            print(display_url)
                """
                print("retweet_hashtages of retweet:   ")
                if "hashtags" in retweet_entities.keys():
                    retweet_hashtages=tweet_read["entities"]["hashtags"]
                    #print(urls)
                    
                    if len (retweet_hashtages) > 0:
                        for retweet_hashtage in retweet_hashtages:
                            retweet_hashtage=retweet_hashtage["text"]
                            
                            
                            print(retweet_hashtage)
                            
                if not "hashtags" in retweet_entities.keys():
                    print("non")
                                   
                    
                
                #tweet object
                tweet_id=tweet_read["retweeted_status"]["id"]
                if "text" in tweet_read.keys():
                    tweet_text=tweet_read["retweeted_status"]["text"]
                    #print("one tweet:   ")
                    #print(tweet_text)
                else:
                    tweet_text=tweet_read["retweeted_status"]["full_text"]
                    #print("one tweet:   ")
                    #print(tweet_text)
                    
                #tweet_entities=tweet_read["retweeted_status"]["entities"]
                tweet_urls=tweet_read["retweeted_status"]["entities"]["urls"]
                if len (tweet_urls) > 0:
                    #print("one tweet:   ")
                   # print(tweet_text)
                    for tweet_url in tweet_urls:
                        url=tweet_url["url"]
                            
                        expanded_url=tweet_url["expanded_url"]
                        display_url=tweet_url["display_url"]
                        #print("url of tweets:   ")
                        #print(url)
                        #print(expanded_url)
                        #print(display_url)
                #print(entities.keys())
                
                """
                if "urls" in tweet_entities.keys():
                    tweet_urls=tweet_read["retweeted_status"]["entities"]["urls"]
                    #print(tweet_urls)
                    
                    if len (tweet_urls) > 0:
                        print("one tweet:   ")
                        print(tweet_text)
                        for tweet_url in tweet_urls:
                            url=tweet_url["url"]
                            
                            expanded_url=tweet_url["expanded_url"]
                            display_url=tweet_url["display_url"]
                            print("url of tweets:   ")
                            print(url)
                            print(expanded_url)
                            print(display_url)
                  """  
                #else:
                    #continue
                    #print("not")
                    
                #tweet_truncated=tweet_read["retweeted_status"]["truncated"]
                #print(tweet_truncated)
                
                print(read)
            else:
                continue
            
    print(read)      
except Exception as e: print(e)       
        
