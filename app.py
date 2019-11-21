
import streamlit as st
import pandas as pd

import vader_wrapper, gcloud_wrapper, textblob_wrapper, corenlp_wrapper

st.title('Language intensity')

st.text('Input some words to see how their strength is evaluated by different tools')

n_fields = st.slider('How many input fields', 3, 10, 3)

default_words = {
    1: 'ok', 
    2: 'good', 
    3: 'excellent'
}

data = [{
    'w': st.text_input(f'w{i}', default_words.get(i, ''), key=i)
} for i in range(1,n_fields + 1)]

gcloud_all_results = gcloud_wrapper.analyse_sentences([el['w'] for el in data])
for a, b in zip(data, gcloud_all_results):
    a['google_cloud'] = b

table = []
for el in data:
    vader_res = vader_wrapper.sentiment_analyzer_scores(el['w'])
    textblob_res = textblob_wrapper.analyse_sentence(el['w'])
    corenlp_res = corenlp_wrapper.get_sentiment(el['w'])

    el['vader_sentiment'] = vader_res
    el['textblob'] = textblob_res
    #el['gcloud'] = gcloud_res
    el['corenlp'] = corenlp_res

table = pd.DataFrame([el for el in data])

st.table(table)
