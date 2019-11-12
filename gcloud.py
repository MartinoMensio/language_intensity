import json
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcloud_key.json'

#  Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

with open('gcloud_cache.json') as f:
    cache = json.load(f)


def analyse_sentences(sentences):
    sentences = [s if s else '#' for s in sentences]
    text = '. '.join(sentences) + '. '
    print(sentences)
    if all([s in cache.keys() for s in sentences]):
        return [cache[k] for k in sentences]
    else:
        sents_analysis = _analyse_text(text)
        sentences_result_dicts = [{
            'text': el.text.content,
            'sentiment': {
                'magnitude': el.sentiment.magnitude,
                'score': el.sentiment.score
            }
        } for el in sents_analysis.sentences]
        assert(len(sentences) == len(sentences_result_dicts))
        for k, v in zip(sentences, sentences_result_dicts):
            cache[k] = v
        with open('gcloud_cache.json', 'w') as f:
            json.dump(cache, f, indent=2)
        return sentences_result_dicts

def _analyse_text(text):
    # The text to analyze
    #text = u'Hello, world!'
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document)#.document_sentiment

    # print('Text: {}'.format(text))
    # print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    print(sentiment)
    return sentiment
