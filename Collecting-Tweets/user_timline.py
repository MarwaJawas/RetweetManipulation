import tweepy
import json
import time
import twitter_keys_access

auth = tweepy.OAuthHandler(twitter_keys_access.CONSUMER_KEY,twitter_keys_access.CONSUMER_SECRET)
auth.set_access_token(twitter_keys_access.ACCESS_TOKEN, twitter_keys_access.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


tweets_read = 0
sn_read = 0
output  = open('%s_%s.json' % ('user_timline', time.strftime('%Y%m%d-%H%M%S')), 'w')


#enter yoyr username
screen_name_list=["@MarwahJawas"]


for screen_name in screen_name_list:
    try:
        
        search =tweepy.Cursor(api.user_timeline, screen_name=screen_name,exclude_replies=False,tweet_mode="extended", include_rts = True).items()
            
    except tweepy.TweepError:
        pass # can't get records from this user, probably a protected account and it is safe to skip
    else:
        for result in search:
            
            tweet = result._json
            json.dump(tweet, output)
            output.write('\n')
            tweets_read += 1
            if tweets_read >= 10000:
                print(tweets_read)
                output.close()
                output  = open('%s_%s.json' % ('user_timline', time.strftime('%Y%m%d-%H%M%S')), 'w')
                tweets_read = 0
                print (tweets_read)
           
