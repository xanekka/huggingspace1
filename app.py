import streamlit as st
from transformers import pipeline

form = st.form(string='inside the form')
user_input = form.text_area('Enter your text')
submit = form.form_submit_button('Submit')

if submit:
    classifier = pipeline("sentiment-analysis")
    result = classifier(user_input)[0]
    label = result['label']
    score = result['score']

    if label == 'POSITIVE':
        st.success(f'{label} sentiment (score: {score})')
    else:
        st.error(f'{label} sentiment (score: {score})')
