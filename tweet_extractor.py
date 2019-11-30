from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pandas as pd
import json
consumer_key="9KSy30k47bFDOT2fKfXWZSzTZ"
consumer_secret="lR645zIuPcNDVgp9h1RaszRkl0vPYKj4DXmZS0GxkvKkGgcIob"
access_token="1200417373729148928-eHpoZwI5bduQ64MBtEq1GugcgWlcjK"
access_token_secret="4vxwdwZQBQnDzrVzcUWxQBB8hN8EkISiDt7QhZDkUvooc"

    
class StdOutListener(StreamListener):
    def on_data(self,data):
        df=pd.read_json(data,orient='records', lines=True)
        pandas_data=pd.DataFrame(df)
        df.to_csv('live_stream_test.csv')
        return True
    
    def on_error(self,status):
        print(status)

if __name__ =="__main__":
    listener=StdOutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    
    stream=Stream(auth,listener)
    stream.filter(track=['Qatar'])
   



