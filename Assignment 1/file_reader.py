import json
import re
import string

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
    tweets_list = []

    with open(file_name, 'r', encoding="utf-8") as f:
        for line in f:
            data = json.loads(line) #data dict
            if "text" in data:
                tweets_list.append(data)
    return tweets_list

#Remove unnecessary whitespaces, return list of words
def extract_words(text):
    text = text.lower()
    word_list =re.split('\W+',text)
    return [ w for w in word_list if len(w) > 0 ]


#def extract_words(text): #str
#    text = strip_punctuation(text) #Substitute punctuations with space
#    clean_text =" ".join(text.split()).lower()  #remove extra whitespace, create clean str
#    words = clean_text.split(" ")       #create list of words
#    return words


#def strip_unicode_punctuation(s):
#    s = s.translate(None, string.punctuation)
#    return s

#def remove_punctuation(text):
#    return re.sub(ur"\p{P}+", "", text)
#    return

#Replace punctuation with SPACE (a.b.c becomes a b c)
#regex = re.compile('[%s]' % re.escape(string.punctuation))
#def strip_punctuation(s):
#    return regex.sub(' ', s)


#test_str = "https://t.co/thrq2ed2so 0.0"
#print(strip_punctuation(test_str))
