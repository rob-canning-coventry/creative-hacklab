

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

careers = [
"Digital Marketing Consultant",
"Junior Front End Designer",
"UX Consultant",
"Interactive Media Designer",
"Mobile Application Developer",
"Augmented Reality Designer",
"Agile Scrum Master #projectmanagement",
"Devops Guru"
]

careertweet = "Thinking about #careerdestinations? how about a " + random.choice(careers) + " http://blablacareerjob.com"

###################################
advantagemodules = [
"Digital and Social Networks",
"",
""
]
optionmodules = [
"Picturing the Body",
"Experimental Narratives: Module leader: Dom Breadmore"
]
optionstweet = "2ndYr, which option module will you choose? " + random.choice(optionmodules) + "?"
advantagetweet = "advantage modules, a great way to broaden your skills! which will you choose? " + random.choice(advantagemodules)
###################################
coremodulesYr1 = ["Transmedia 104MC", "Creative Hacklab 104MC", "Digital Marketing and Campaigns 104MC"]
coremodulesYr2 = ["Transmedia 204MC", "International Creative Hacklab 204MC", "Digital Marketing and Campaigns 204MC"]
coremodulesYr3 = ["Final Project 333MC", "Creative Hacklab III 304MC", " 204MC"]
###################################
generaltweets = [
"I'm the digital media twitter bot! #awesome #code I tweet a couple of times a day..",
"http://coventry.media/digitalmedia #awsome #digitalmedia #degree #uk",
"Studying #digitalmedia in #coventryuni - get some l33t 5k1llz #beyonddigitalliteracy",
"Current running module = Creative Hacklab #104MC",
"#robisawesome",
"#digitalmediacov Lecturers: Adnan Hadzi (Senior Lecturer), Rob Canning (Lecturer in Connected Digital Media)",
"the best #digitalmediacov workshops with #digitalmediacov Associate Lectuer Dan",
"#worldleading #skillssessions with Navneet Bains, Paul Adkins and Becks Stewart #digitalmediacov",
"hello world!",
"#freestuff don't forget to sign up for your https://education.github.com/pack to get your $100 #digitalocean credits"
"learning #git workflows, loving the https://education.github.com/pack",
"https://www.blender.org #blender #3D",
"Vector graphics fun with #inkscape https://inkscape.org/en/",
"#markdown (.md files) a great way to sketch out webpages and take lecture notes!",
"write in markdown then convert to html docx pdf etc with #pandoc #awesomepower",
"#audacity a great tool for making #podcasts",
"#Gimp, perfect for things with pixels, no... not vectors, #rasters!",
"make awsome montages with #imagemagick #commandline fun",
"want #projectmanagement skills? get clued in to Agile using http://tagia.io",
"Want to learn #AdobeCreativeSuite? - don't forget Becks and Nav run a session every #wedensday during term time in ETG05."
]
###################################
readinglist = [
"The Network Society by Manuel Castells",
"The New Media Reader by ",
""
]
readingtweet = "Wondering what to read next? Try " + random.choice(readinglist)
###################################
watchinglist = [
"Internets Own Boy: The story of Aaron Swartz",
"CitizenFour #edwardsnowden",
"The Social Network: The story of Facebook"
]
watchingtweet = "Looking for something to watch tonight? try " + random.choice(watchinglist) + " #itsallresearch"
###################################

commandoftheday = [
"",
""

]



allothertweets = [readingtweet, watchingtweet, careertweet, optionstweet, advantagetweet];

if __name__ == "__main__":
    twitter = TwitterAPI()
    while True:
        tweets = [
        random.choice(generaltweets),
        random.choice(generaltweets),
        random.choice(generaltweets),
        random.choice(allothertweets)]
        for i in tweets:
            print(i);
            #twitter.tweet(i)
            time.sleep(0.01);
