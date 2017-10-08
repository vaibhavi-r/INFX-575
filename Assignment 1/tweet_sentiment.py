
import sys
import pprint as pp
import json


def hw():
    print('Hello, world!')

def lines(fp):
    print (str(len(fp.readlines())))

def main():
    senti_file_name = sys.argv[1]
    tweet_file_name = sys.argv[2]

    sent_file = open(senti_file_name)
    tweet_file = open(tweet_file_name)
    hw()

    print("\nNumber of Affinity words in %s : " %senti_file_name)
    lines(sent_file)

    print("\nNumber of Tweets collected in %s : " %tweet_file_name)
    lines(tweet_file)

    #Parse sentiment and tweet files to generate scores
    sentiment = read_sentiment_file(senti_file_name)
    tweets_list = read_tweet_file(tweet_file_name)
    tweet_scores = score_tweets(sentiment, tweets_list)

    print("\nNumber of Tweets with text : \n%d " % (len(tweets_list)))
    print("\nNumber of Tweets scored    : \n%d " %(len(tweet_scores)))


#Read Sentiment Data
def read_sentiment_file(file = "AFINN-111.txt"):
    data = {}
    with open(file) as f:
        for line in f:
            (key, val) = line.strip().split("\t")
            data[key] = int(val)
    return data


#Read JSON Data
def read_tweet_file(file = "output.txt"):
    ctr = 0
    tweets_list = []

    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            data = json.loads(line) #data dict
            if "text" in data:
                tweets_list.append(data)
    return tweets_list

#Extract text from tweet
def extract_text(d):
    return d["text"]


#Score the tweets
def score_tweets(sentiment, tweets_list ):
    score_list = []
    for tweet in tweets_list:
        score=0
        words = extract_text(tweet).split(" ")
        for w in words:
            score+= sentiment.get(w,0)
        score_list.append(int(score))
    return score_list

if __name__ == '__main__':
    main()

