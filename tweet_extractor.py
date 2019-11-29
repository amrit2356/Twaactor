from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

    
class StdOutListener():
    def on_data(self,data):
        print(data)
        return true
    
    def on_error(self,data):
        print(status)

if __name__ =="__main__":
    listener=StdOutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    
    stream=Stream(auth,listener)
    stream.filter(track=['falcon','Qatar'])


