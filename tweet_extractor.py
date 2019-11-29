from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import twitter_credentials

class TwitterStreamer():
    def stream_tweets(self, fetched tweets_filename, hash tag list):
        pass 
    
    def on_data(self,data):
        print(data)
        return true

    def off_data(self,data):
        print(status)


