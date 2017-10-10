import sys
import tweet_sentiment as tw
import file_reader as fr


def main():
    senti_file_name = sys.argv[1]
    tweet_file_name = sys.argv[2]

    #Read input files
    tweets_list = fr.read_tweet_file(tweet_file_name)
    sentiment   = fr.read_sentiment_file(senti_file_name)

    #Find all new terms, store scores of associated tweets
    new_terms = find_new_terms(sentiment, tweets_list)

    #Calculate sentiments for new terms
    new_term_scores = calculate_new_term_sentiments(new_terms)

    #print to stdout
    for new_term, score in new_term_scores.items():
        print(new_term, score)


#Returns dictionary of new terms with list of associated tweet scores
def find_new_terms(sentiment, tweets_list):
    tweet_scores = tw.score_tweets(sentiment,tweets_list )
    new_terms = {}

    for i in range(len(tweets_list)):
        tweet = tweets_list[i]
        score = tweet_scores[i]

        text = tweet["text"]
        words = fr.extract_words(text)  #Removes multi-spaces,\n, \r from messy tweet
        for w in words:
            if w not in sentiment: #unscored word
                if w not in new_terms:  #unscored and unseen before
                    new_terms[w] = [score]
                else: #seen before, currently unscored
                    new_terms[w].append(score)

    return new_terms

#Scoring Metric: Average sentiment of a tweet containing new term
def calculate_new_term_sentiments(new_terms):

    new_term_scores = {}
    #val is list of associated tweet scores
    for term, val in new_terms.items():
        new_term_scores[term] = sum(val) / len(val)
    return new_term_scores

if __name__ == '__main__':
    main()
