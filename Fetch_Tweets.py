import sys,tweepy

def twitter_auth():
    try:
        consumer_key = 'gUIDkKRp9wg8kaHOUZL5xVCLX'
        consumer_secret = '5l8Olmtl9W9xzXh6vsOxU734vOUGLIFSMwr2AAfG7GcgCVbcva'
        access_token = '1196705023805116416-xAHAA3gYfMkp8vTR0M41TJtvU7f6yl'
        access_secret = 'JCwaSq5gY7x4WL07Lbdo7YnxDNe1puxxuxAZZEg4gtI9V'
    except KeyError:
        sys.stderr.write("TWITTER_* environment variable not set\n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth
def get_twitter_client():
    auth = twitter_auth()
    client = tweepy.API(auth,wait_on_reate_limit=True)
    return client

if __name__ == '__main__':
    user = input("Enter username:")
    client = get_twitter_client()
    for status in tweepy.Cursor(client.home_timeline, screen_name=user).items():
        print(status.text)
    
