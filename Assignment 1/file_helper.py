import json

#Read Sentiment Data
def read_sentiment_file(file = "AFINN-111.txt"):
    data = {}
    with open(file) as f:
        for line in f:
            (key, val) = line.strip().split("\t")
            data[key] = int(val)
    return data


#Read JSON Data
def read_tweet_file(file = "output.txt"):
    ctr = 0
    tweets_list = []

    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            data = json.loads(line) #data dict
            if "text" in data:
                tweets_list.append(data)
    return tweets_list


#Extract text from tweet dict
def extract_text(d):
    return d["text"]

