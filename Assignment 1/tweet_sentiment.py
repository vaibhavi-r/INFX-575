import sys
import file_reader as fr

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

#    print("\nNumber of Affinity words in %s : " %senti_file_name)
    lines(sent_file)

#    print("\nNumber of Tweets collected in %s : " %tweet_file_name)
    lines(tweet_file)

    #Parse sentiment and tweet files to generate scores
    sentiment = fr.read_sentiment_file(senti_file_name)
    tweets_list = fr.read_tweet_file(tweet_file_name)
    tweet_scores = score_tweets(sentiment, tweets_list)


#Score the tweets
def score_tweets(sentiment, tweets_list ):
    score_list = []
    for tweet in tweets_list:
        score=0
        words = tweet["text"].split(" ")
        for w in words:
            score+= sentiment.get(w,0)
        score_list.append(int(score))
    return score_list

if __name__ == '__main__':
    main()

