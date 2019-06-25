import csv
import tweepy
from twitter import Twitter, OAuth, TwitterHTTPError
import time



consumer_key = 'XXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXX'
access_token_key = 'XXXXXXXXXXXXXX-XXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXX'


t = Twitter(auth=OAuth(access_token_key, access_token_secret,
                       consumer_key, consumer_secret))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)


TWITTER_HANDLE = 'YourTwitterUserName' ####Need to change
user = api.get_user(TWITTER_HANDLE)

RECORD_BY_STAGES_DIR = 'C:/Users/XXXXXXXXXXXXXX/Documents/TwitterBotGame/record-by-stages/'

following = set(api.friends_ids())
followers = set(user.followers_ids())

set_s = set.intersection(followers, following)

s_file_path = RECORD_BY_STAGES_DIR + 's.csv'

with open(s_file_path, "w") as out_file:
    for val in set_s:
        out_file.write(str(val) + "\n")


set_s_prime = following - set_s

s_prime_file_path = RECORD_BY_STAGES_DIR + 's-prime.csv'

with open(s_prime_file_path, "w") as out_file:
    for val in set_s_prime:
        out_file.write(str(val) + "\n")



for user_id in set_s:

    try:
        api.destroy_friendship(user_id)
        print("unfollowed %d" % (user_id))
        time.sleep(90)
    except tweepy.TweepError as error:
        print(type(error))

        if str(error) == 'Not authorized.':
            print('Can''t access user data - not authorized.')
            continue

        if str(error) == 'User has been suspended.':
            print('User suspended.')
            continue

        errorObj = error.args[0][0]

        print(errorObj)

        if errorObj['message'] == 'Rate limit exceeded':
            print('Rate limited. Sleeping for 15 minutes.')
            time.sleep(15 * 60 + 15)
            continue

for user_id in set_s_prime:

    try:
        api.destroy_friendship(user_id)
        print("unfollowed %d" % (user_id))
        time.sleep(90)
    except tweepy.TweepError as error:
        print(type(error))

        if str(error) == 'Not authorized.':
            print('Can''t access user data - not authorized.')
            continue

        if str(error) == 'User has been suspended.':
            print('User suspended.')
            continue

        errorObj = error.args[0][0]

        print(errorObj)

        if errorObj['message'] == 'Rate limit exceeded':
            print('Rate limited. Sleeping for 15 minutes.')
            time.sleep(15 * 60 + 15)
            continue
