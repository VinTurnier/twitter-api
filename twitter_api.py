import twitter 
import os

consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token_key = os.environ.get('TWITTER_ACCESS_TOKEN_KEY')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token_key,
                  access_token_secret=access_token_secret)

results = api.GetSearch(
    raw_query="q=twitter%20donaldtrump&result_type=recent&count=100")

for result in results:
    data = {
        'user_name':result.user.name,
        'user_location':result.user.name,
        'user_tweet':result.text
    }
    print(data)


# class Status(object):
#     user = User()
#     text = Text()

# resuts [Status()...]
