import streamlit as st

from headliner.model.summarizer_transformer import SummarizerTransformer

summarizer = SummarizerTransformer.load('model/')

st.title('English-German Translator')
st.markdown('''
This is a demo showcasing our [Headliner package](). In particular, we trained
a simple seq2seq model on an English-German dataset. We didn't train it very long so
the model is not doing well as this was not our main goals anyway. For creating the app,
we use [Streamlit](https://streamlit.io/), a new open-source framework that lets users creating
apps for machine learning projects very easily.
''')
input = st.text_input(label='Type in some English words.', value='How are you?')
st.write(summarizer.predict(input))
