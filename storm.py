	

# AnonStorm twitterstorm bot
#
# Usage: python storm.py --access_token_key <twitter access_token_key> --access_token_secret <twitter access_token_secret>
#                        --tweet_file_url <tweet_file_url>  (optional; if not used, will default to AnonStorm/TweetLog.txt)
#
# IF YOU RECEIVED THIS SCRIPT FROM ANOTHER LOCATION OTHER THAN GITHUB.COM/SOMER4NDOMPUNK THEN YOU WILL BE USING AN OUTDATED AND
# POTENTIALLY DANGEROUS VERSION OF THIS SCRIPT. NEVER EVER EVER DOWNLOAD SHIT FROM A FILE HOST, YOU CAN NOT VERIFY THE CODE
# UNTIL YOU DOWNLOAD IT, BY THEN, IT COULD BE TOO LATE!!
#
# A VERY special thanks to The, Happyface, Prophet and kyzersane for their work on this script, hosting the script, and hosting the tweet file.
# Without each of your feed backs this project would never have become a reality.
#
# Version 1.0
 
import time, datetime, sched, random, argparse
import urllib2
import twitter
 
def main(args):
    print("Welcome to AnonStorm v1.0 | If you did not download this from SomeR4ndomPunks GitHub then you are outdated and at risk! Enjoy\n")
    # Do not edit consumer_key nor consumer_secret. These are used by Twitters API
    api=twitter.Api(consumer_key="5VuZ39FbuRfFdr0CpNf3zg",consumer_secret="5FPi40pwS3buTMFMXm8URXoRSCubw0LqM5KtTPkdo",access_token_key=args.access_token_key,access_token_secret=args.access_token_secret)
         
    contents=[]
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    s  = sched.scheduler(time.time, time.sleep)
     
    def do_something(sc):
        if args.tweet_file_url:
            try:
                response = urllib2.urlopen(args.tweet_file_url)
                contents = response.readlines()
            except:
                print("Error loading text file contents. Ensure http:// prepends your url.")
        else:
            try:
                with open("TweetLog.txt") as f:
                    contents = f.readlines()
            except:
                print("Looks like you moved TweetLog.txt and did not specify a tweet file URL with the --tweet_file_url option... Try again.")
                return
 
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
 
if __name__=="__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--access_token_key",required=True,type=str,help="Twitter access token key (see file for instructions)")
    arg_parser.add_argument("--access_token_secret",required=True,type=str,help="Twitter access token secret (see file for instructions)")
    arg_parser.add_argument("--tweet_file_url",type=str,help="URL for new line delimited text file of tweets")
    args = arg_parser.parse_args()
    main(args)

