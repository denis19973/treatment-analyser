import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

PROCESS_TWEETS_PER_CANDIDATE = 1500

CONSUMER_KEY = ''
CONSUMER_SECRET = ''

ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def search_tweets(query):
	return tweepy.Cursor(api.search,
                           q=query,
                           count=100,
                           result_type="recent",
                           include_entities=False,
                           lang="en").items()

def analyse_text_sentiment(text):
	text_blob = TextBlob(text)
	return text_blob.sentiment.polarity

def plot_sentiment(text, sentiment_value):
    plt.scatter(text, sentiment_value, color='black')

def process_and_plot(text):
    processed = 0
    value = 0
    for tweet in search_tweets(text):
        processed += 1
        sentiment = analyse_text_sentiment(tweet.text)
        value += sentiment
        if processed >= PROCESS_TWEETS_PER_CANDIDATE:
        	break
    plot_sentiment(text, value/processed)

plt.ylabel('Sentiment')
plt.title('Treatment to Candidates')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

process_and_plot('Zelenskiy')
process_and_plot('Timoshenko')
process_and_plot('Poroshenko')

plt.legend()
plt.show()
