#filter only retweet object and then store and insert data from json file into sqlite3
import sqlite3 as lite
import sys
import json


    
with open('Rest_retweet_20190922-120345.json','r') as fh:
    for i in range(10):
        line = next(fh)
        
        if line.strip():
            tweet_read=json.loads(line)
                
            if "retweeted_status" in tweet_read.keys():
                
                    #tweet object
                if "text" in tweet_read.keys():
                    tweet_text=tweet_read["retweeted_status"]["text"]
                    print(tweet_text)
                    
                    
                else:
                    tweet_text=tweet_read["retweeted_status"]["full_text"]
                    print(tweet_text)
            
            else:
                continue        
             
        else: 
            continue
print("finishing...") 
        