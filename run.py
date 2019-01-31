import tweepy
import matplotlib.pyplot as plt
import indicoio

PROCESS_TWEETS_PER_CANDIDATE = 3000
PROCESS_TEXT_PER_REQUEST = 100

indicoio.config.api_key = ''

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
                           lang="ru").items()

def analyse_text_sentiment(texts: list):
	sentiments = indicoio.sentiment(texts, language='detect')
	return [s for s in sentiments if s is not None]

def plot_sentiment(text, sentiment_value):
    plt.scatter(text, sentiment_value, color='black')

def process_and_plot(text):
    processed = 0
    sentiment_value = 0
    tweets_chunk = []
    for tweet in search_tweets(text):
        tweets_chunk.append(tweet.text)
        if len(tweets_chunk) == PROCESS_TEXT_PER_REQUEST:
            sentiments = analyse_text_sentiment(tweets_chunk)
            sentiment_value += sum(sentiments)
            processed += len(sentiments)
            tweets_chunk = []
        if processed >= PROCESS_TWEETS_PER_CANDIDATE:
          break
    if tweets_chunk:
        sentiments = analyse_text_sentiment(tweets_chunk)
        sentiment_value += sum(sentiments)
        processed += len(sentiments)
    if processed:
      sentiment = sentiment_value / processed
      plot_sentiment(text, sentiment)

plt.ylabel('Sentiment(0 - negative, 1 - positive)')
plt.title('Treatment to Candidates')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

process_and_plot('Зеленский')
process_and_plot('Тимошенко')
process_and_plot('Порошенко')

plt.legend()
plt.show()
