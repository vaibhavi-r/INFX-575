import json

#Read sentiment data, return dictionary
def read_sentiment_file(file_name = "AFINN-111.txt"):
    data = {}
    with open(file_name) as f:
        for line in f:
            (key, val) = line.strip().split("\t")
            data[key] = int(val)
    return data


#Read tweet JSON data, return list of tweets
def read_tweet_file(file_name = "output.txt"):
    ctr = 0
    tweets_list = []

    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            data = json.loads(line) #data dict
            if "text" in data:
                tweets_list.append(data)
    return tweets_list

