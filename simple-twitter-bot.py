import tweepy
import random
import time
from time import sleep

CONSUMER_KEY = 'xxxx'
CONSUMER_SECRET = 'xxxx'
ACCESS_TOKEN = 'xxxx-xxxx'
ACCESS_TOKEN_SECRET = 'xxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

search_results = api.search(q="keyword", count=100)
 
sentences = ['sentence one', 'sentence two', 'sentence three', 'sentence four']

for s in search_results:
        message = random.choice(sentences)
        sn = s.user.screen_name
        m = "@%s " % (sn) + str(sentences)
        s = api.update_status(m, s.id)
        sleep(900)
 