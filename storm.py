# Twitter Storm Python Bot
#
# This script is released with no license. Fuck that. Edit and use as you wish
# This script, as it sits will pull from an online file located on The's webhost.
# It will pull a random tweet from the hosted file, and tweet every 2 minutes a new random tweet.
# 
# You MUST run the auth.py script first to obtain your access_token_key and your access_token_secret. This will authorize the app with your twitter account.
# Once you verify the pin, you MUST update the appropriate strings access_token_key and access_token_secret with the key and secret auth.py gives you.
#
# A VERY special thanks to The, Happyface, Prophet and kyzersane for their work on this script, hosting the script, and hosting the tweet file.
# Without each of your feed backs this project would never have become a reality.
#
# Version 0.5b RC1
#
# http://www.anonymous101.tk/tweetstorm0.5b.zip

import time, datetime, sched, random
import urllib2
import twitter
     
print('Welcome to TwitterStorm v0.5b RC1')
# Do not edit consumer_key nor consumer_secret. These are used by Twitters API
api=twitter.Api(consumer_key='5VuZ39FbuRfFdr0CpNf3zg',consumer_secret='5FPi40pwS3buTMFMXm8URXoRSCubw0LqM5KtTPkdo',access_token_key='YOUR_ACCESS_TOKEN_HERE',access_token_secret='YOUR_ACCESS_SECRET_HERE')
     
contents=[]
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
s  = sched.scheduler(time.time, time.sleep)
 
def do_something(sc):
        response = urllib2.urlopen('https://github.com/somer4ndompunk/AnonStorm/blob/master/TweetLog.txt')
        contents = response.readlines()
 
        while True:
                try:
                        print("Tweeting...", st)
                        print("", contents[random.randint(0,len(contents)-1)])
                        status = api.PostUpdate(contents[random.randint(0,len(contents)-1)])
                        break
                except twitter.TwitterError as e:
                        print("Twitter error received...", e.message)
                        print("Trying again...")
 
        sc.enter(120, 1, do_something, (sc,)) #Edit the "120" if you wish to speed or slow down the tweets. Time is in seconds. IE: 120 = 2 minutes
 
s.enter(0, 1, do_something, (s,))
s.run()

