import json
import csv
import tweepy
import re

import nltk
from textblob import TextBlob

#Its not a scrapper but tried to call a twitter API to get sentiment analysis on a perticular hashtag
def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    avg_pol=0
    item=10
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)

    for tweet in tweepy.Cursor(api.search, q=hashtag_phrase, tweet_mode='extended').items(item):
        obj=TextBlob(tweet.full_text.replace('\n',' '))
        polarity = obj.sentiment.polarity
        avg_pol+=polarity
    print('Avg polarity: ',avg_pol/10)
    if avg_pol/item >0:
        print('Average sentiment of tweets is positive')
    elif avg_pol/item == 0.0:
        print('Average sentiment of tweets is neutral')        
    else:
        print('Average sentiment of tweets is negative')
        

#######
c_k=input('consumer_key')
c_s=input('consumer_secret')
a_t=input('access_token')
a_t_s=input('access_token_secret')
#h_p='marvel'
#####
consumer_key = c_k.encode(encoding='utf-8')
consumer_secret = c_s.encode(encoding='utf-8')
access_token = a_t.encode(encoding='utf-8')
access_token_secret = a_t_s.encode(encoding='utf-8')
hashtag_phrase = 'marvel'.encode(encoding='utf-8')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
    