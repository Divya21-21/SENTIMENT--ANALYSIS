from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize VADER
analyzer = SentimentIntensityAnalyzer()

# Example Sentences
sentences = [
    "I love this product!",
    "This is the worst service ever.",
    "I'm not sure how I feel about this.",
    "Absolutely fantastic experience!",
    "It was okay, nothing special."
]

# Analyze Sentiment
for sentence in sentences:
    score = analyzer.polarity_scores(sentence)
    compound = score['compound']
    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    print(f"{sentence}\n → Sentiment: {sentiment}, Score: {compound:.2f}\n")
