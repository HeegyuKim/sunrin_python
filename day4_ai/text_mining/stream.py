#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "254502682-SzniNN2L3NwMgZ0XtXeEsHZQbY2dTVXS95pgYo3E"
access_token_secret = "bF4bShp16UvPhBTiAKAIqxabhbNWIA1MA3M6kRh1v6fYP"
consumer_key = "avDU7U1c3bPbuwcR7YHooKfWa"
consumer_secret = "S6sfN0yJapGvJ13QeE0khu7Z4rTmOOs7YIyX6e76yOupE53L7F"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    f = open('languages.txt', 'w')

    def on_data(self, data):
        print data
        self.f.write(data + str('\n'))
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])