# Twitter-bot-follow-unfollow-other-users
This repo is a part of a project on Twitter bot and game theory. If you find this code useful in your research, please consider citing:

@InProceedings{chenGameSec2018,
author="Chen, Jundong
and Hossain, Md Shafaeat
and Brust, Matthias R.
and Johnson, Naomi",
editor="Bushnell, Linda
and Poovendran, Radha
and Ba{\c{s}}ar, Tamer",
title="A Game Theoretic Analysis of the Twitter Follow-Unfollow Mechanism",
booktitle="Decision and Game Theory for Security",
year="2018",
publisher="Springer International Publishing",
address="Cham",
pages="265--276",
isbn="978-3-030-01554-1"
}

Use bot_follow_users.py to setup a Twitter bot and follow other Twitter users.

There is a limit on Twitter about following limit in a unit time, and per day. I saved all the Twitter ids into 6 days, and each day includes 1000 ids.
If you need to follow more Twitter accounts, you need to do it in more days.

The basic idea is as follows.

Step 1: import the ids from each csv file which stores the ids, then save it as list and then convert the list to a set.
For example:

atu_list_1 = []
with open(ALL_TWITTER_USERS_DAY1) as in_file:
    for line in in_file:
        atu_list_1.append(int(line))

atu_set_1 = set(atu_list_1)

Step 2: to follow other accounts with the api method create_friendship. Also need to record the now time in order to be able to continue to the next day after finishing the today's work.
For example:

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
