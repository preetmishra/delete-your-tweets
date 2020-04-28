import os
import tweepy


# Replace these with your keys and secrets.
CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('TWITTER_ACCESS_KEY')
ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

screen_name = input('Enter your screen name (without the hashtag): ')
user = api.get_user(screen_name=screen_name)

tweets = api.user_timeline(id=user.id, include_rts=True)
for tweet in tweets:
    print('Deleting tweets...')
    api.destroy_status(tweet.id)
