from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey='1Vwj1tv5JoT5yJX2N70C4lyhx'
csecret='DRXIIgL8yPi6Ko2DHGT8WQeGuaWdKgzOkE4siwM0FtafrjxUTA'
atoken='745704821412462593-hukfpWg2RQQUSR7FgSxHvlqwF8zNZ7v'
asecret='M6Cc0hikFC66Wk3Mw0baMzfKHe3C7eQCJJoKjdyFEuZvZ'
class listener(StreamListener):
    def on_status(self, status):
        if(status.place.country_code=="ID"):
            file=open('output.txt', 'a')
            string=""
            print("STATUS_ID:"+str(status.id))
            string=string+"STATUS_ID:"+str(status.id)+"\n"
            print("STATUS_TEXT:"+str(status.text))
            string=string+"STATUS_TEXT:"+str(status.text)+"\n"
            print("USERNAME:"+str(status.user.screen_name))
            string=string+"USERNAME:"+str(status.user.screen_name)+"\n"
            print("COORD:"+str(status.coordinates))
            string=string+"STATUS_ID:"+str(status.coordinates)+"\n"
            print("PLACE:"+str(status.place.full_name))
            string=string+"STATUS_ID:"+str(status.place.full_name)+"\n\n"
            print("\n\n")
            file.write(string)
            file.close()
        else:
            print("PICKED UP TWEETS FROM INCORRECT LOCATION!!")
            print("PLACE:"+str(status.place.full_name))
            print("\n\n")

    def on_error(self,status):
        print(status)


auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken, asecret)
twitterStream=Stream(auth, listener())

#track can be used to mention keywords that we may be looking for
#locations an be used to specify the geo-locations of the source of the tweets
#follow can be used to look for tweets from specific users
#there are other such provisions in the API too which can be used as per need
twitterStream.filter(locations=[104.76,-4.955, 105.24,-4.95])
file.close()
