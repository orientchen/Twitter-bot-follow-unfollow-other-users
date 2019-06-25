import csv
import tweepy
from twitter import Twitter, OAuth, TwitterHTTPError
import time



consumer_key = 'XXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXX'
access_token_key = 'XXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXX'


t = Twitter(auth=OAuth(access_token_key, access_token_secret,
                       consumer_key, consumer_secret))

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)


TWITTER_HANDLE = 'orientchen1978'
user = api.get_user(TWITTER_HANDLE)

RECORD_BY_STAGES_DIR = 'C:/Users/XXXXXXXXXXXXXXXXXX/Documents/TwitterBotGame/record-by-stages/'

following = set(api.friends_ids())
followers = set(user.followers_ids())

set_s = set([])

s_file_path = RECORD_BY_STAGES_DIR + 's.csv'

#file_path = source_dir + str(i) + '.csv'
with open(s_file_path, 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        set_s.update(row)
#######

set_s1 = set.intersection(set_s, followers)

s1_file_path = RECORD_BY_STAGES_DIR + 's1.csv'

with open(s1_file_path, "w") as out_file:
    for val in set_s1:
        out_file.write(str(val) + "\n")

set_s2 = set_s - set_s1

s2_file_path = RECORD_BY_STAGES_DIR + 's2.csv'

with open(s2_file_path, "w") as out_file:
    for val in set_s2:
        out_file.write(str(val) + "\n")



for user_id in set_s2:

    try:
        api.create_friendship(user_id)
        print("followed %s" % (user_id))
        time.sleep(30)
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
