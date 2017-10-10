import sys
import file_reader as fr

def main():
    tweet_file_name = sys.argv[1]
    tweets_list = fr.read_tweet_file(tweet_file_name)

    hist = calculate_frequency(tweets_list)
    ctr = 0
    for term, freq in hist.items():
        print(term, freq)


def calculate_frequency(tweets_list):
    histogram = {}
    total_words = 0

    for tweet in tweets_list:
        text = tweet["text"]
        words = fr.extract_words(text)
        for w in words:
            total_words += 1
            if w not in histogram:
                histogram[w] = 1
            else:
                freq = histogram[w]
                histogram[w] = freq +1

    for w in histogram:
        count = histogram[w]
        histogram[w] = count/total_words
    return histogram


if __name__ == '__main__':
    main()
