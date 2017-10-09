import sys
import file_reader as fr

def hw():
    print('Hello, world!')

def lines(fp):
    print(str(len(fp.readlines())))


def main():
    tweet_file_name = sys.argv[1]

    tweet_file = open(tweet_file_name)
    hw()

    lines(tweet_file)
    tweets_list = fr.read_tweet_file(tweet_file_name)

    hist = calculate_frequency(tweets_list)
    ctr = 0
    for key in hist:
        ctr +=1
        if ctr < 10:
            print(key,  " -  " , hist[key])


def calculate_frequency(tweets_list):
    histogram = {}
    total_words = 0

    for tweet in tweets_list:
        words = tweet["text"].split()
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
