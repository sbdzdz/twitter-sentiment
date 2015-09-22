from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Cursor, Stream, API, TweepError
import json

consumer_key='IvEafIljD0uiiTdyFGEg5pFBf'
consumer_secret = 'CNDkyfbaLHGDMy1dpWPMDtgSPhExHO2GRPR3WIRnCDNMeiWPXK'
access_token='2664299401-2zZ0A79mmLw3BwxkfdytHPvyf62tM1XPsm061ZW'
access_token_secret='mPiLgSIBNtzPF0jtQ0FxwnOCwQVMaINnyTHwAvZJwFmoP'

class StdOutListener(StreamListener):

        def on_data(self, data):
                print data

        def on_error(self, error_code):
                print error_code
                return True

        def on_timeout(self):
                print 'Timeout!'
                return True

        def on_disconnect(self):
                print 'Disconnected'
                return True

            
def streamTweets(keywords, languages):
        listener = StdOutListener()
        authentication = OAuthHandler(consumer_key, consumer_secret)
        authentication.set_access_token(access_token, access_token_secret)
        stream = Stream(authentication, listener)
        stream.filter(track=keywords, languages=languages)

def findTweets(keywords):
        authentication = OAuthHandler(consumer_key, consumer_secret)
        authentication.set_access_token(access_token, access_token_secret)
        api = API(authentication)
        cursor = Cursor(api.search, q=keywords).items()
        while True:
                try:
                        tweet = cursor.next()
                        print ','.join([str(tweet.created_at), tweet.lang, tweet.text]).encode('utf-8')
                except TweepError:
                        time.sleep(60 * 15)
                        continue
                except StopIteration:
                        break


if __name__== "__main__":
        keywords=['na', 'w', 'o', 'na', 'to', 'z', 'i', 'do', 'nie', 'to', 'lub']
        languages=['pl']
        streamTweets(keywords, languages)

