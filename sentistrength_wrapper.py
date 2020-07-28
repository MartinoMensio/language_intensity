from sentistrength import PySentiStr

senti = PySentiStr()
senti.setSentiStrengthPath('data/sentistrength/SentiStrength5.jar')
senti.setSentiStrengthLanguageFolderPath('data/sentistrength/SentStrength_Data')


def analyse_sentence(sentence):
    return senti.getSentiment(sentence)