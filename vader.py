from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re
import string
analyzer = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(text):
    score = analyzer.polarity_scores(text)
    print(text)
    print(score)
    return score


if __name__ == "__main__":
    sentiment_analyzer_scores('ok')
    sentiment_analyzer_scores('good')
    sentiment_analyzer_scores('excellent')
