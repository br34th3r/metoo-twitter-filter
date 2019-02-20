import tweepy

key = "xxx"
secret = "xxx"
access_token = "xxx"
access_secret = "xxx"

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MeTooListener(tweepy.StreamListener):
    def on_status(self, status):
        with open("tweets.txt", "a") as file:
            file.write(status.text + "\n\n")
            file.close()

meTooListenerObject = MeTooListener()
meTooStream = tweepy.Stream(auth=api.auth, listener=meTooListenerObject)

meTooStream.filter(track=['#MeToo'])
