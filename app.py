import vader
import gcloud
import streamlit as st

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

gcloud_all_results = gcloud.analyse_sentences([el['w'] for el in data])
for a, b in zip(data, gcloud_all_results):
    a['gcloud'] = b

table = []
for el in data:
    vader_res = vader.sentiment_analyzer_scores(el['w'])

    el['vader'] = vader_res
    #el['gcloud'] = gcloud_res

table = [
    [el['w'], el['vader'], el['gcloud']] for el in data
]

st.table(table)
