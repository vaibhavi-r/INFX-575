import sys
import tweet_sentiment as tweets
from file_helper import *


def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))


def main():
    senti_file_name = sys.argv[1]
    tweet_file_name = sys.argv[2]

    sent_file = open(senti_file_name)
    tweet_file = open(tweet_file_name)
    hw()

    lines(sent_file)
    lines(tweet_file)

    tweets_list = read_tweet_file(tweet_file_name)
    sentiment =   read_sentiment_file(senti_file_name)

    new_term_scores = calculate_new_term_sentiments(sentiment, tweets_list)
    print(len(new_term_scores))


def find_new_terms(sentiment, tweets_list):
    tweet_scores = tweets.score_tweets(sentiment,tweets_list )
    new_terms = {}

    for i in range(len(tweets_list)):
        tweet = tweets_list[i]
        score = tweet_scores[i]

        words = tweet["text"].split(" ")
        for w in words:
            if w not in sentiment: #unscored word
                if w not in new_terms:  #unseen before
                    new_terms[w] = [score]
                else: #seen before
                    new_terms[w].append(score)

    print(len(new_terms))
    return new_terms


def calculate_new_term_sentiments(sentiment, tweets_list):

    new_terms = find_new_terms(sentiment, tweets_list)

    new_term_scores = {}
    for term , val in new_terms.items():
        new_term_scores[term] = sum(val) / len(val)  #Average sentiment of a tweet containing new term

    return new_term_scores



if __name__ == '__main__':
    main()
