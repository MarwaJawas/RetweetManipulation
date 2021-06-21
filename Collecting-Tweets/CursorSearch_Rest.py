import tweepy
import json
import time
import twitter_keys_access

def cursorSearch(search_words):
    auth = tweepy.OAuthHandler(twitter_keys_access.CONSUMER_KEY,twitter_keys_access.CONSUMER_SECRET)
    auth.set_access_token(twitter_keys_access.ACCESS_TOKEN, twitter_keys_access.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

    #F_NAME = 'mp_retweet_data_(%s_to_%s).json' % (start_date.isoformat(), end_date.isoformat())

    tweets_read = 0
    sn_read = 0

    output  = open('%s_%s.json' % ('Rest_retweet', time.strftime('%Y%m%d-%H%M%S')), 'w')


      
    for search_word in search_words:
        print(search_word)    
        try:
            for status in tweepy.Cursor(api.search,q = search_word,tweet_mode="extended").items():
                tweet = status._json
                json.dump(tweet, output)
                output.write('\n')
                tweets_read += 1
                if tweets_read >= 10000:
                    print(tweets_read)
                    output.close()
                    output  = open('%s_%s.json' % ('Rest_retweet', time.strftime('%Y%m%d-%H%M%S')), 'w')
                    tweets_read = 0 
            #search=tweepy.Cursor(api.search,q = search_words,tweet_mode="extended").items(MAX_TWEETS)
            #except Exception as e: print(e)
        except tweepy.TweepError:
            pass 
       

#enter your search words 
search_words=["#  ",
           "#  " ,
             "# "]  

cursorSearch(search_words)
