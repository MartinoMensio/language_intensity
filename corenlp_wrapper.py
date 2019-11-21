from pycorenlp import StanfordCoreNLP

# https://towardsdatascience.com/sentiment-analysis-beyond-words-6ca17a6c1b54
# http://nlp.stanford.edu:8080/sentiment/rntnDemo.html

nlp = StanfordCoreNLP('http://localhost:9000')

def get_sentiment(text):
    res = nlp.annotate(text,
                       properties={'annotators': 'sentiment',
                                   'outputFormat': 'json',
                                   'timeout': 5000,
                       })
    print(text)
    print('Sentiment:', res['sentences'][0]['sentiment'])
    print('Sentiment score:', res['sentences'][0]['sentimentValue'], '/ 4 (0 is most negative, 4 is most positive)')
    print('Sentiment distribution (0-v. negative, 5-v. positive:', res['sentences'][0]['sentimentDistribution'])
    sentence_result = res['sentences'][0]
    return {
        'sentimentValue': sentence_result['sentimentValue'],
        'sentiment': sentence_result['sentiment'],
        'sentimentDistribution': sentence_result['sentimentDistribution'],
        'sentimentTree': sentence_result['sentimentTree'],
    }



if __name__ == '__main__':
    res = get_sentiment('I am happy')
