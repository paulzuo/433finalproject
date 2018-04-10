import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'EbJtNnQkdS97Dxq3xTMvNSEOq'
consumer_secret = 'SQ6tXAtydVElC5vg9toOG4BTn1YlXVtI2Gd2l2ApQdPVb5hdlO'
access_token = '271213536-81XI80NUifREyfA1rj75HlQqPnMrC5e95Mzad4zL'
access_token_secret = 'YOhy8TXRIoFI2z1Gsz46ChDJxqg34agVaFQahshwn3MNc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])