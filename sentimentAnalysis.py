import tweepy
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as mp
from tkinter import *
import time

# Twitter application credentials
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# Assigning the credentials to the OAuthHandeler
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

# Creating an API object
api=tweepy.API(auth)

# Variables to store positive, negative and neutral counts
pos_count = 0
neg_count = 0
neutral_count = 0



# Variable to store the search element
search_keyword=''

# Calling the search method

pubic_tweets=api.search(search_keyword,count=100)

# Variable to store the fancy characters in a tweet
girl_words=['@','RT',':','https','http','#', '/', '\\']
# symbols=['@','#']

data=[]

pos_count = 0
neg_count = 0
neutral_count = 0
mixed_count = 0
record_count = 1

for tweet in pubic_tweets:
    # Getting/Storing only the text field
    text_data=tweet.text
    

    # Tokenizing the text field where each word is a token
    print("Text data after tokenizing record ", record_count)
    textWords = word_tokenize(text_data)
    print (textWords)

    # Refining the text field using the concept of regular expression
    cleanedTweet = ' '.join(re.sub("([^0-9A-Za-z \t])|(@[A-Za-z0-9]+)|(RT)|(\w+:\/\/\S+)", " ", text_data).split())

    #english here specifies the list of stop words in english
    stop_words = set(stopwords.words("english"))
    print('Text data after removing stop words in record ', record_count)
    print(stop_words)
    other_list = ["'", ':', ',', '.','?', '!']

    print (cleanedTweet)

    analysis= TextBlob(cleanedTweet)
    # print (analysis.sentiment)
    # Clearly Positive	"score": 0.8, "magnitude": 3.0
    if analysis.sentiment.polarity>0.25:
        polarity = 'Clearly Positive'
        pos_count += 1
    # Clearly Negative	"score": -0.6, "magnitude": 4.0
    if(analysis.sentiment.polarity < -0.15):
        polarity = 'Clearly Negative'
        neg_count += 1
    # Neutral	"score": 0.1, "magnitude": 0.0
    if(-0.15 > analysis.sentiment.polarity <=0.12):
        polarity = 'Neutral'
        neutral_count += 1
    # Mixed	"score": 0.0, "magnitude": 4.0
    if( analysis.sentiment.polarity == 0):
        polarity = 'Mixed'
        mixed_count += 1

    polarity_data = []
    polarity_data.append(polarity)
    print(polarity)
    
    print()
    print('------------------------------------------------------------------------------------------------------------')
    print()
    record_count += 1

print('Number of tweets analyzed ',len(pubic_tweets))
print()
print("===============================================================================================================")
print("Analysis result..")
print('Clearly Positive',pos_count)
print('Clearly Negative',neg_count)
print('Neutral',neutral_count)
print('Mixed reviews', mixed_count)
print("Opening the chart...")
time.sleep(2)
print('Done :)')
labels = 'Positive','Negative','Neutral','Mixed'
sizes = [pos_count,neg_count,neutral_count,mixed_count]
colors = ['green', 'red','yellow','pink']
explode = [0.1,0,0,0]

mp.pie( sizes, explode=explode, labels=labels, colors=colors,startangle=90, autopct='%.1f%%')
mp.axis('equal')
mp.title("Sentiment Chart")
mp.show()

