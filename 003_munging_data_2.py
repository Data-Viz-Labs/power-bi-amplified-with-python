import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
	if pd.isna(text):
		return None

	blob = TextBlob(str(text))
	return blob.sentiment.polarity

# Apply sentiment analysis to the column with name 'comment_textDisplay'
dataset['sentiment_score'] = dataset['comment_textDisplay'].apply(analyze_sentiment)
