from textblob import TextBlob


def analyse_sentence(sentence):
    blob = TextBlob(sentence)
    print(blob.sentiment)
    return blob.sentiment



if __name__ == '__main__':
    res = analyse_sentence('I am happy')
