import streamlit as st

from headliner.model.summarizer_transformer import SummarizerTransformer
from headliner.model.summarizer_attention import SummarizerAttention

summarizer_transformer = SummarizerTransformer.load('model/transformer')
summarizer_attention = SummarizerAttention.load('model/attention')

st.title('English-German Translator')
st.markdown('''
This is a demo showcasing our [Headliner package](). In particular, we trained
a simple seq2seq model on an English-German dataset. We didn't train it very long so
the model is not doing well as this was not our main goals anyway. For creating the app,
we use [Streamlit](https://streamlit.io/), a new open-source framework that lets users creating
apps for machine learning projects very easily.
''')
input = st.text_input(label='Type in some English words.', value='I really like you.')
st.write('(transformer) {}'.format(summarizer_transformer.predict(input)))
st.write('(attention) {}'.format(summarizer_attention.predict(input)))
