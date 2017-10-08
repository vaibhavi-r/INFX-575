import pprint as pp
import json

def read_tweet_file(file = "problem_1_submission.txt"):
    ctr = 0
    tweets_list = []

    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            data = json.loads(line) #data dict
            pp.pprint(data)
            print("\n-----------------------------")
            if "text" in data:
                tweets_list.append(data)



read_tweet_file()
