import json
import re
from itertools import ifilterfalse

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

with open('tweets') as tweets:
    for line in tweets:
        try:
            tweet = json.loads(line)
            timestamp = tweet['created_at']
            text = normalise(tweet['text'])
            print text
#            print ','.join([timestamp, text])
        except ValueError:
            continue
        except KeyError:
            continue
