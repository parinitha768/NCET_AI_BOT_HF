import streamlit as st
from transformers import pipeline
def load_summarizer():
  return pipline("Summarization", model="sshleifer/distilbart-cnn-12-6")
summarizer=load_summrizer()
st.title("AI Text Summarizer")
st.write("Enter a long text below, and get a concise summary!")
long_text=st.text_area("Enter text to summarize:",height=200)
max_length=st.slider("Max Summary Length",min_value=50,
                     max_value=300,value=130 ")
min_length=st.slider("Min Summary Length", min_value=20,
                     max_value=100,value=30 ")
if st.button("Summarizer"):
  if long_text.strip():
    with st.spinner("Generating summary..."):
      summary=summarizer(long_text, max_length=max_length,
                         min_length=min_length,do_sample=false)
      st.subheader("Summary:")
      st.success(summary[0]['summary_text'])
else:
  st.warning("Please enter some text to summarize")
