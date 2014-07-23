import sys
import json

def get_sentiment(phrase, sent_dict):
	sentiment = 0
	for word in phrase.split():
		sentiment += sent_dict.get(word, 0)
	return sentiment

def generate_sent_dict(sent_file):
	sent_dict = {}
	for line in sent_file:
		term, sentiment = line.split("\t")
		sent_dict[term] = int(sentiment)
	return sent_dict

def main():
	with open(sys.argv[1]) as sent_file:
		sent_dict = generate_sent_dict(sent_file) 
	with open(sys.argv[2]) as tweet_file:
		for line in tweet_file.readlines():
			phrase = json.loads(line)['text']
			print get_sentiment(phrase, sent_dict)

if __name__ == '__main__':
	main()
