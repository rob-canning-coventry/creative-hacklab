import tweepy
import random
import time
class TwitterAPI:
    def __init__(self):
        consumer_key = "4MDOBG8vdmPI0TiCswH1QfJ2k"
        consumer_secret = "7UjfZ5HvmB8pcuEz0R2eDUExxxxxxxxxxxxxxxx"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "732845932816019456-DNmUqdpEZaBOotqQo76Z0DAD5l1mCow"
        access_token_secret = "k6xq6xxxxxxxxxxxxxxxxxgxfBecYpeS"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

ta = "I'm the digital media twitter bot! #awesome #code I tweet a couple of times a day.."
tb = "http://coventry.media/digitalmedia #awsome #digitalmedia #degree #uk"
tc = "Studying #digitalmedia in #coventry"
td = "Current running module = Creative Hacklab #104MC"
te = "#robisawesome"
tf = "hello world!"
tg = "learning #git workflows, loving the https://education.github.com/pack"
th = "https://www.blender.org #blender #3D"
th = "Vector graphics fun with #inkscape https://inkscape.org/en/"

tweets = [ta, tb, tc, td, te, tf, tg, th];

if __name__ == "__main__":
    twitter = TwitterAPI()
    #while True:
    for i in tweets:
        print(i);
        twitter.tweet(i)
        time.sleep(3600.0);
