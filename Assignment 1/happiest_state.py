import sys
import file_helper as fh
import tweet_sentiment as tw
import states as st
import pprint as pp


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

    tweets_list = fh.read_tweet_file(tweet_file_name)
    sentiment =   fh.read_sentiment_file(senti_file_name)
    tweet_scores = tw.score_tweets(sentiment, tweets_list)

    states_dict = init_states_count()
    states_dict = gather_geotagged_tweets(tweets_list, tweet_scores, states_dict)

    states_scores = calculate_state_scores(states_dict)
    #pp.pprint(states_scores)

    print("Happiest State = ", get_happiest_state(states_scores))

def get_happiest_state(states_scores):
    max_state = max(states_scores, key=lambda k: states_scores[k])
    return st.states[max_state]

def init_states_count():
    states_dict = {}
    for s in st.states:
        states_dict[s] = []
    return states_dict


def gather_geotagged_tweets(tweets_list, tweet_scores, states_dict):
    ctr3=0
    ctr4=0
    valid_ctr3 = 0

    for i in range(len(tweets_list)):
        tweet = tweets_list[i]
        score = tweet_scores[i]

        case3=[]

        #Case 3:
        if "user" in tweet:
            ctr3+=1
            if "location" in tweet["user"]:
                location = tweet["user"]["location"]
                if location is not None:
                    s = location.strip(" ")[-2:]
                    if s.isupper():
                        #print(s)
                        if s in st.states:
                            valid_ctr3 += 1
                            states_dict[s].append(score)
        else:
            ctr4+=1

    print("Total tweets: " , len(tweets_list))
    print("Tweets with user : ", ctr3)
    print("Tweets with user location : ", valid_ctr3)
    print("Tweets with neither", ctr4)

    return states_dict

def calculate_state_scores(states_dict):
    states_scores = {}
    for s in states_dict:
        total = sum(states_dict[s])
        if len(states_dict[s]) ==0:
            states_scores[s] = 0
        else:
            states_scores[s] = total/len(states_dict[s])
    return states_scores


if __name__ == '__main__':
    main()
