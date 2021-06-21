import tweepy
import json
import time
import twitter_keys_access
import os

auth = tweepy.OAuthHandler(twitter_keys_access.CONSUMER_KEY,twitter_keys_access.CONSUMER_SECRET)
auth.set_access_token(twitter_keys_access.ACCESS_TOKEN, twitter_keys_access.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

retweets_read = 0
tweet_id_list=[]

output  = open('%s_%s.json' % ('retweet_status_of_tweet', time.strftime('%Y%m%d-%H%M%S')), 'w')

with open('rt.txt','r') as fh:
        
    for line in fh:    
        ids_read=json.loads(line)
        tweet_id_list.extend(ids_read)
#print(tweet_id_list)

#tweet_id_list=[1199649079686582272,1199555428956491777,1199598685321076736]
               
for tweet_id in tweet_id_list:
    #print(tweet_id)
    #r=0    
    try:
        for status in api.retweets(id=tweet_id,count=100,tweet_mode="extended"): 
            r+=1
            tweet = status._json
            json.dump(tweet, output)
            output.write('\n')
            retweets_read += 1
            if retweets_read >= 10000:
                print(retweets_read)
                output.close()
                output  = open('%s_%s.json' % ('retweet_status_of_tweet', time.strftime('%Y%m%d-%H%M%S')), 'w')
                retweets_read = 0 
        #print("ret:  ",r)
    #except Exception as e: print(e)    
    except tweepy.TweepError:
        pass 
          
