import json
import re
from itertools import ifilterfalse
from collections import defaultdict
import operator

def removeHyperlinks(text):
    return ' '.join(ifilterfalse(lambda x:x.startswith(("http://", "https://")), text.split()))

def removeUserMentions(text):
    return ' '.join(ifilterfalse(lambda x:x.startswith(("@")), text.split()))

def removeHashtags(text):
    return ' '.join(ifilterfalse(lambda x:x.startswith(("#")), text.split()))

def removeNonAlpha(text):
    return re.sub(ur'[\W_]+', u' ', text, flags=re.UNICODE)

def removeRT(text):
    return text.replace('RT', '')

def normalise(text):
    text = removeHyperlinks(text)
    text = removeUserMentions(text)
    text = removeHashtags(text)
    text = removeNonAlpha(text)
    text = removeRT(text)
    return text.lower().strip()

def getUserMentions(tweet):
    return [user['screen_name'] for user in tweet['entities']['user_mentions']]

def getHashtags(tweet):
    return[hashtag['text'] for hashtag in tweet['entities']['hashtags']]

def getPopularUserMentions(file):
    count = defaultdict(int)
    with open(file) as tweets:
        for line in tweets:
            try:
                tweet = json.loads(line)
                for user in getUserMentions(tweet):
                    count[user] += 1
            except ValueError:
                continue
            except KeyError:
                continue
    return sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)

def getPopularHashtags(file):
    count = defaultdict(int)
    with open(file) as tweets:
        for line in tweets:
            try:
                tweet = json.loads(line)
                for hashtag in getHashtags(tweet):
                    count[hashtag] += 1
            except ValueError:
                continue
            except KeyError:
                continue
    return sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)

if __name__ == "__main__":
    for key, value in getPopularUserMentions('tweets')[:500]:
        print key, ':', value
#     with open('tweets') as tweets:
#         for line in tweets:
#             try:
#                 tweet = json.loads(line)
#                 text = normalise(tweet['text'])
#                 timestamp = tweet['created_at']
#                 print ','.join([timestamp, text])
#             except ValueError:
#                 continue
#             except KeyError:
#                 continue
