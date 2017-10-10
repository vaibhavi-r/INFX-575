import sys
import file_reader as fr

def main():
    tweet_file_name = sys.argv[1]

    #Read input tweets file
    tweets_list = fr.read_tweet_file(tweet_file_name)
    hashtag_counts = calculate_top_ten_hashtags(tweets_list)

    #convert to sorted list of tuples
    sorted_hashtag_counts =  sorted(hashtag_counts.items(), key=lambda t: t[1], reverse = True)

    #print up to 10 top hashtags to stdout
    limit = len(sorted_hashtag_counts)
    if limit > 10:
        limit = 10

    for i in range(limit):
        hashtag,count = sorted_hashtag_counts[i]
        print(hashtag, count)

    #print(sorted_hashtag_counts[:10])


def calculate_top_ten_hashtags(tweets_list):
    hashtag_counts = {}
    total_hashtags = 0

    for tweet in tweets_list:
        if "entities" in tweet:
            entities = tweet["entities"]
            if entities is not None and "hashtags" in entities:
                hashtags = entities["hashtags"]  #list

                for ht in hashtags:
                    total_hashtags +=1
                    text = ht["text"]

                    if text not in hashtag_counts:
                        hashtag_counts[text] = 1
                    else:
                        count = hashtag_counts[text]
                        hashtag_counts[text] = count+1
    return hashtag_counts

if __name__ == '__main__':
    main()
