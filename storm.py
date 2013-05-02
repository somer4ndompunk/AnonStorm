# AnonStorm twitterstorm bot
#
# IF YOU RECEIVED THIS SCRIPT FROM ANOTHER LOCATION OTHER THAN GITHUB.COM/SOMER4NDOMPUNK THEN YOU WILL BE USING AN OUTDATED AND
# POTENTIALLY DANGEROUS VERSION OF THIS SCRIPT. NEVER EVER EVER DOWNLOAD SHIT FROM A FILE HOST, YOU CAN NOT VERIFY THE CODE
# UNTIL YOU DOWNLOAD IT, BY THEN, IT COULD BE TOO LATE!!
#
# This script, as it sits will pull from an online file.
# It will pull a random tweet from the hosted file, and tweet every 2 minutes a new random tweet.
# 
# You MUST run the auth.py script first to obtain your access_token_key and your access_token_secret. This will authorize the app with your twitter account.
# Once you verify the pin, you MUST update the appropriate strings access_token_key and access_token_secret with the key and secret auth.py gives you.
#
# A VERY special thanks to The, Happyface, Prophet and kyzersane for their work on this script, hosting the script, and hosting the tweet file.
# Without each of your feed backs this project would never have become a reality.
#
# Version 1.0

import time, datetime, sched, random
import urllib2
import twitter
     
print('Welcome to AnonStorm v1.0 | If you did not download this from SomeR4ndomPunks GitHub then you are outdated and at risk! Enjoy')
# Do not edit consumer_key nor consumer_secret. These are used by Twitters API
api=twitter.Api(consumer_key='5VuZ39FbuRfFdr0CpNf3zg',consumer_secret='5FPi40pwS3buTMFMXm8URXoRSCubw0LqM5KtTPkdo',access_token_key='YOUR_ACCESS_TOKEN_HERE',access_token_secret='YOUR_ACCESS_SECRET_HERE')
     
contents=[]
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
s  = sched.scheduler(time.time, time.sleep)
 
def do_something(sc):
        response = urllib2.urlopen('LINK_TO_OP_TWEET_FILE')
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

