import sys
import file_reader as fr
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

    #Prepare list of tweets, and sentiment words and scores for all tweets
    tweets_list = fr.read_tweet_file(tweet_file_name)
    sentiment =   fr.read_sentiment_file(senti_file_name)
    tweet_scores = tw.score_tweets(sentiment, tweets_list)

    #Assign Tweets to states if possible
    states_dict = assign_state_to_tweets(tweets_list)

    #Calculate sentiment scores for each state
    #Metric: Finding Average Sentiment of tweets generated in a state, Default = 0
    statewise_scores = calculate_state_scores(states_dict, tweet_scores)
    #pp.pprint(statewise_scores)


    #Find Happiest State (Most positive average sentiment)
    happiest_state = get_happiest_state(statewise_scores)
    print(happiest_state)

def assign_state_to_tweets(tweets_list):

    #initialize all states with empty list of tweets
    states_dict = {}
    for s in st.US_codes:
        states_dict[s] = []

    #Go over tweets and check "place" or "user" location
    for idx in range(len(tweets_list)):
        tweet = tweets_list[idx]
        found_state = False  #Whether state was found for the tweet


        #Check PLACE
        if "place" in tweet and tweet["place"] is not None:
            place = tweet["place"]
            if "country_code" in place and place["country_code"] == "US":
                if "place_type" in place:
                    place_type = place["place_type"]

                    if place_type =="admin":
                        if "name" in place:
                            name = place["name"]

                            code = st.get_state_code(name)
                            if code is not None:
                                found_state = True
                                states_dict[code].append(idx)

                    elif place_type =="city":
                        if "full_name" in place:
                            full_name = place["full_name"]

                            words = full_name.strip(" ").split(" ") #Full Name Format = 'Austin, TX'
                            code = words[-1]

                            if code in st.US_codes:
                                found_state = True
                                states_dict[code].append(idx)


        #CHECK USER defined LOCATION
        if found_state ==False and "user" in tweet and  tweet["user"] is not None and "location" in tweet["user"]:
            location = tweet["user"]["location"]
            if location is not None:
                words = location.strip(" ").split(" ")
                code = words[-1]
                if code in st.US_codes:
                    found_state= True
                    states_dict[code].append(idx)

    return states_dict


def calculate_state_scores(states_dict, tweet_scores):
    statewise_scores = {}

    for s in states_dict:
        tweets_from_state = states_dict[s]
        statewise_scores[s]=0

        n = len(tweets_from_state)
        if n > 0:
            for idx in tweets_from_state:
                statewise_scores[s] += tweet_scores[idx]
            statewise_scores[s] = statewise_scores[s]/n

    return statewise_scores

#Return the Full Name of the state with highest average sentiment of tweets
def get_happiest_state(statewise_scores):
    max_state = max(statewise_scores, key=lambda k: statewise_scores[k])
    return st.US_codes[max_state]


if __name__ == '__main__':
    main()
