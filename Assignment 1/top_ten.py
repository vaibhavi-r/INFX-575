import sys
import file_helper as fh

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))



def main():
    tweet_file_name = sys.argv[1]

    tweet_file = open(tweet_file_name)
    hw()

    lines(tweet_file)
    tweets_list = fh.read_tweet_file(tweet_file_name)

    hashtag_counts = calculate_top_ten_hashtags(tweets_list)
    sorted_hashtag_counts =  sorted(hashtag_counts.items(), key=lambda t: t[1], reverse = True)

    print(sorted_hashtag_counts[:10])


def calculate_top_ten_hashtags(tweets_list):
    hashtag_counts = {}
    total_hashtags = 0

    for tweet in tweets_list:
        if "entities" in tweet:
            entities = tweet["entities"]
            if "hashtags" in entities:
                hashtags = entities["hashtags"]

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
