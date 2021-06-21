from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from slistener import SListener
from urllib3.exceptions import ProtocolError
import twitter_keys_access

def streamingTweet(keywords_to_hear):

    # consumer key authentication
    auth = OAuthHandler(twitter_keys_access.CONSUMER_KEY, twitter_keys_access.CONSUMER_SECRET)
    # access key authentication

    auth.set_access_token(twitter_keys_access.ACCESS_TOKEN, twitter_keys_access.ACCESS_TOKEN_SECRET)
    # set up the API with the authentication handler
    api = API(auth)
    # set up words to hear

    
    # instantiate the SListener object
    listen = SListener(api)

    # instantiate the stream object
    stream = Stream(auth, listen)



    # begin collecting data
    while True:
        # maintian connection unless interrupted
        try:
            stream.filter(track=keywords_to_hear)
        # reconnect automantically if error arise
        # due to unstable network connection
        except (ProtocolError, AttributeError):
            continue
            
        
#call method
keywords_to_hear = ['#االراتب',
                    '#الهلال_الاتحاد_دوري_اسيا',
                    '#الاتحاد_الهلال'
                   ]

streamingTweet(keywords_to_hear)
