#Install tweepy: python -m pip install tweepy --user

#import twitter_credentials
import GetOldTweets3 as got
import pandas as pd

 

tweetCriteria = got.manager.TweetCriteria().setQuerySearch("falcons, Qatar")\
                                           .setSince("2015-01-01")\
                                           .setUntil("2016-01-01")\
                                           .setMaxTweets(500)

                    
print("Done stream")
username = {}
text = {}
date = {}
location = {}
print("Done arrays")
for i in range(468, 500):
    tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
    username[i] = tweet.username
    text[i] = tweet.text
    date[i] = tweet.date
    location[i] = tweet.geo
    Falcons = {"User" : username, "Text" : text, "Date" : date, "Location" : location}
    df = pd.DataFrame(Falcons)
    falcon_csv = df.to_csv(r'falcon5_4.csv')
    print("Done: {}".format(i))