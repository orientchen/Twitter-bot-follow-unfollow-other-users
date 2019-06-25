import tweepy
from twitter import Twitter, OAuth, TwitterHTTPError
import datetime
import json
import time
import os


consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

TWITTER_HANDLE = 'YourTwitterUserName'
ALREADY_FOLLOWED_FILE = "already-followed.csv"
user = api.get_user(TWITTER_HANDLE)

ALL_TWITTER_USERS_DAY1 = "C:/Users/XXXXXXXXXX/Documents/TwitterBotGame/Bot1-Bot2-lists/Bot2/bot2-different-days/day1.csv"
ALL_TWITTER_USERS_DAY2 = "C:/Users/XXXXXXXXXX/Documents/TwitterBotGame/Bot1-Bot2-lists/Bot2/bot2-different-days/day2.csv"
ALL_TWITTER_USERS_DAY3 = "C:/Users/XXXXXXXXXX/Documents/TwitterBotGame/Bot1-Bot2-lists/Bot2/bot2-different-days/day3.csv"
ALL_TWITTER_USERS_DAY4 = "C:/Users/XXXXXXXXXX/Documents/TwitterBotGame/Bot1-Bot2-lists/Bot2/bot2-different-days/day4.csv"
ALL_TWITTER_USERS_DAY5 = "C:/Users/XXXXXXXXXX/Documents/TwitterBotGame/Bot1-Bot2-lists/Bot2/bot2-different-days/day5.csv"
ALL_TWITTER_USERS_DAY6 = "C:/Users/XXXXXXXXXX/Documents/TwitterBotGame/Bot1-Bot2-lists/Bot2/bot2-different-days/day6.csv"



atu_list_1 = []
with open(ALL_TWITTER_USERS_DAY1) as in_file:
    for line in in_file:
        atu_list_1.append(int(line))

atu_set_1 = set(atu_list_1)

atu_list_2 = []
with open(ALL_TWITTER_USERS_DAY2) as in_file:
    for line in in_file:
        atu_list_2.append(int(line))

atu_set_2 = set(atu_list_2)

atu_list_3 = []
with open(ALL_TWITTER_USERS_DAY3) as in_file:
    for line in in_file:
        atu_list_3.append(int(line))

atu_set_3 = set(atu_list_3)

atu_list_4 = []
with open(ALL_TWITTER_USERS_DAY4) as in_file:
    for line in in_file:
        atu_list_4.append(int(line))

atu_set_4 = set(atu_list_4)

atu_list_5 = []
with open(ALL_TWITTER_USERS_DAY5) as in_file:
    for line in in_file:
        atu_list_5.append(int(line))

atu_set_5 = set(atu_list_5)

atu_list_6 = []
with open(ALL_TWITTER_USERS_DAY6) as in_file:
    for line in in_file:
        atu_list_6.append(int(line))

atu_set_6 = set(atu_list_6)



now = datetime.datetime.now()

from datetime import timedelta

count = 0
for twitter_id in atu_set_1:
    print("Day 1:")
    try:
        api.create_friendship(twitter_id)
    except Exception as e:
        print("error: %s" % (str(e)))
    count = count + 1
    print("followed number of users: "+str(count))
    time.sleep(60)

while True:
    current = datetime.datetime.now()
    if current - now >= timedelta(hours=24):
        now = datetime.datetime.now()
        break

count = 0
for twitter_id in atu_set_2:
    print("Day 2:")
    try:
        api.create_friendship(twitter_id)
    except Exception as e:
        print("error: %s" % (str(e)))
    count = count + 1
    print("followed number of users: "+str(count))
    time.sleep(60)

while True:
    current = datetime.datetime.now()
    if current - now >= timedelta(hours=24):
        now = datetime.datetime.now()
        break

count = 0
for twitter_id in atu_set_3:
    print("Day 3:")
    try:
        api.create_friendship(twitter_id)
    except Exception as e:
        print("error: %s" % (str(e)))
    count = count + 1
    print("followed number of users: "+str(count))
    time.sleep(60)

while True:
    current = datetime.datetime.now()
    if current - now >= timedelta(hours=24):
        now = datetime.datetime.now()
        break

count = 0
for twitter_id in atu_set_4:
    print("Day 4:")
    try:
        api.create_friendship(twitter_id)
    except Exception as e:
        print("error: %s" % (str(e)))
    count = count + 1
    print("followed number of users: "+str(count))
    time.sleep(60)

while True:
    current = datetime.datetime.now()
    if current - now >= timedelta(hours=24):
        now = datetime.datetime.now()
        break

count = 0
for twitter_id in atu_set_5:
    print("Day 5:")
    try:
        api.create_friendship(twitter_id)
    except Exception as e:
        print("error: %s" % (str(e)))
    count = count + 1
    print("followed number of users: "+str(count))
    time.sleep(60)

while True:
    current = datetime.datetime.now()
    if current - now >= timedelta(hours=24):
        now = datetime.datetime.now()
        break

count = 0
for twitter_id in atu_set_6:
    print("Day 6:")
    try:
        api.create_friendship(twitter_id)
    except Exception as e:
        print("error: %s" % (str(e)))
    count = count + 1
    print("followed number of users: "+str(count))
    time.sleep(60)

while True:
    current = datetime.datetime.now()
    if current - now >= timedelta(hours=24):
        now = datetime.datetime.now()
        break





