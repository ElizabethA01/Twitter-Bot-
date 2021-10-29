from logging import error
from re import search
import tweepy
import time

auth = tweepy.OAuthHandler('5U7adKCbcGiNFVXqFiHRfZ1fk', 'cpnAFjh0X1Ng7p81IY52OVevGQHidwK9MFZEtG2F1n9NPV4gxN')
auth.set_access_token('414156523-WUhJuLXH4gPSQdW8IYACiV9wZUjYpFr2dUdVWlwy','NjMavF2SgCWZbbfwXtT6ke1WE35f7ro2jayk4TjWNe7wc')

api = tweepy.API(auth)
user = api.me()

search_string = 'python'
numbersoftweets = 2
names_string = 'Kelly'

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

def tweet_favourite(search_text, no_of_tweets):
    #A bot that likes certain tweets
    for tweet in limit_handler(tweepy.Cursor(api.search, search_text).items(no_of_tweets)):
        try:
            tweet.favorite()
            print('I liked that tweet')
        except tweepy.TweepError as err:
            print(err.reason)
        except StopIteration:
            break


def followback(names):
    #A bot that follows back
    for follower in limit_handler(tweepy.Cursor(api.followers).items()):
        if follower.name == names:
            print('Found!')
            follower.follow()
            break

followback(names_string)
tweet_favourite(search_string, numbersoftweets)
 