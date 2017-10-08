import sys
import tweet_sentiment

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




if __name__ == '__main__':
    main()
