import sys
import file_reader as fr


def main():
    senti_file_name = sys.argv[1]
    tweet_file_name = sys.argv[2]

    #Parse sentiment and tweet files to generate scores
    sentiment = fr.read_sentiment_file(senti_file_name)
    tweets_list = fr.read_tweet_file(tweet_file_name)
    tweet_scores = score_tweets(sentiment, tweets_list)

    if(len(tweet_scores) != len(tweets_list)):
        print("Error occurred in scoring tweets.", len(tweet_scores) )

    #print results to stdout
    for score in tweet_scores:
        print(score)

#Score the tweets
def score_tweets(sentiment, tweets_list ):
    score_list = []
    for tweet in tweets_list:
        score=0
        text = tweet["text"]
        words = fr.extract_words(text)  #Removes multi-spaces,\n, \r from messy tweet
        for w in words:
            score+= sentiment.get(w,0)
        score_list.append(int(score))
    return score_list

if __name__ == '__main__':
    main()

