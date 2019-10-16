# Headliner Demo

This is a demo showcasing our [Headliner package](https://github.com/as-ideas/headliner). In particular, we trained
a simple seq2seq model on an English-German dataset. We didn't train it very long so
the model is not doing well as this was not our main goals anyway. For creating the app,
we use [Streamlit](https://streamlit.io/), a new open-source framework that lets users creating
apps for machine learning projects very easily.

In fact, for the deployment, we only need six lines of code:
```python
import streamlit as st
from headliner.model.summarizer_transformer import SummarizerTransformer

summarizer_transformer = SummarizerTransformer.load('model/transformer')

st.title('Type in some English')
title = st.text_input('How are you?')
st.write(summarizer_transformer.predict(title))
```

## 🚀 Quick Start

1. Install all the packages:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the demo:
    ```bash
    streamlit run translation_demo.py
    ```
3. View the Streamlit app in your browser: `http://localhost:8501`

## © Copyright

See [LICENSE](LICENSE) for details.