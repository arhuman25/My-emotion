from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

text = input("Enter text: ")
sentiment = analyze_sentiment(text)
if sentiment == "Positive":
    print(f"{sentiment}: You're energetic and postive. Keep going!")
elif sentiment == "Negative":
    print(f"{sentiment}: You aren't doing great, right now.")
elif sentiment == "Neutral":
    print(f"{sentiment}: A neutral mind is an ideal mind")
else:
    print(f"{sentiment}: You don't seem to have a unstable emotion")