#integrate our code with open ai

import os
from constants import openai_key

# from langchain.llms import openai
from langchain_community.llms import openai

import streamlit as st

os.environ['OPENAI_API_KEY']=openai_key
#streamlit framework

st.title("Langchain Demo with open ai api")
input_text=st.text_input("Search the topic")

#if someone types a text then it should interact with the open ai

#open ai llm
llm=openai.OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))