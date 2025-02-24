"""
Performs sentiment analysis on text comments using TextBlob.
For Power BI: Requires TextBlob installation in Power BI's Python environment.
Input: DataFrame with 'comment_textDisplay' column
Output: Adds 'sentiment_score' column (-1 to 1 scale)
Note: Handles NaN values automatically
"""

import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
	if pd.isna(text):
		return None

	blob = TextBlob(str(text))
	return blob.sentiment.polarity

# Apply sentiment analysis to the column with name 'comment_textDisplay'
dataset['sentiment_score'] = dataset['comment_textDisplay'].apply(analyze_sentiment)
