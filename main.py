# ATTENTION: Add a file called settings.py with appropriate settings
# as imported below.

import tweepy
from settings import consumer_key, consumer_secret, access_token, access_token_secret, hashtag


print ("Authenticating.")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print ("Authenticated.")
print ("Now fetching tweets.")

tweets = api.search(q=hashtag)
print ("fetched all tweets")
print ()

counter = {}
users = {}

for t in tweets:
    if t.user.id in counter:
        counter[t.user.id] += 1
    else:
        counter[t.user.id] = 1
        users[t.user.id] = t.user

tuple_list = counter.items()
tuple_list = sorted(tuple_list, key=lambda x: x[1], reverse=True)
name_list = [(users[x[0]].name, x[1]) for x in tuple_list]

i = 1
print ("Leaderboard:")
print ("-"*80)
for name, count in name_list[:10]:
    print ("{0}. {1} with {2} tweets".format(i, name, count))
    i += 1

