import tweepy
import string
import re
import json

class accountTimeline:
    def __init__(self):
        return

    def analyzeTweet(self, tweet):
        listing = ("Lists" in tweet)
        return listing

    def getTweets(self, api):
        #Add here the list of official twitter accounts
        #user_timeline api call parameters
        screenName = "@binance_2017"
        count = 100
        tweetList = {}
        tweetDate = ""
        tweetText = ""

        print("Obtaining tweets from {}".format(screenName))
        timeline = api.user_timeline(screen_name = screenName, count=count)

        timelineStr = json.dumps([tw._json for tw in timeline], indent=4)
        #print(timelineStr)
        timelineJSON = json.loads(timelineStr)

        for tw in range(len(timelineJSON)):
            tweetText = timelineJSON[tw]['text'].encode('utf-8')
            createdAt = timelineJSON[tw]['created_at'].encode('utf-8')
            listing = self.analyzeTweet(tweetText)
            if (listing):
                result = re.search('Lists(.*)\((.+?)\)', str(tweetText))
                coinListed = result.group(1)
                coinListed = coinListed.replace("#","")
                coinSymbol = result.group(2)
                coinSymbol = coinSymbol.replace('$','')
                print("Coin Listed: {}".format(coinListed))
                print("Coin Symbol: {}".format(coinSymbol))
                print("Text: {}".format(str(tweetText)))
                print("Created At: {}\n".format(str(createdAt)))


        return 0

    def setupOAuth(self):
        consumer_key = "xXBydi6MkwSsXx5u0Czc7w6hV"
        consumer_secret = "95qyLGE7zgdkab3dhtj2oOu2YOclOxrKWrUh0U9BSBHrrRZueG"

        access_token = "965803882541649921-gzhO3q1cMmXrCQaP5EABGJTVnsrvPcb"
        access_secret = "V6jJtLSGbYXOx0YyB99ROtVQBuXWrTKv5gJ3FS2BAI747"

        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_secret)
            api = tweepy.API(auth)

            print("Successfully authenticated twitter app")
            print(api.me().name)

            return api
        except Exception as e:
            print("Unable to authenticate: ", e)


    def main(self):
        api = self.setupOAuth()
        self.getTweets(api)

if __name__ == "__main__":
    tweet = accountTimeline()
    tweet.main()