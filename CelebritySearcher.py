#integrate our code with open ai

import os
from constants import openai_key

# from langchain.llms import openai
from langchain_community.llms import openai
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

#this sequential is used to combine all the the chains produced to give a sequence of output 
from langchain.chains import SequentialChain


os.environ['OPENAI_API_KEY']=openai_key
#streamlit framework

st.title("Langchain Demo with open ai api")
input_text=st.text_input("Search the topic")



#prompt template

first_input_prompt=PromptTemplate(input_variables=['name'],template="Tell me about celebrity {name}")

#if someone types a text then it should interact with the open ai

#open ai llm
llm=openai.OpenAI(temperature=0.8)

chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='person')

second_input_prompt=PromptTemplate(input_variables=['name'],template="when was {name} born")

chain2=LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='dob')


parent_chain=SequentialChain(chains=[chain,chain2],input_variables=['name'],output_variables=['person','dob'] ,verbose=True)

third_input_prompt=PromptTemplate(input_variables=['dob'],template="Give 5 great even held on {dob}")
chain3=LLMChain(llm=llm,prompt=third_input_prompt,verbose=True,output_key='description')

parent_chain=SequentialChain(chains=[chain,chain2,chain3],input_variables=['name'],output_variables=['person','dob','description'] ,verbose=True)

if input_text:
    st.write(parent_chain({'name':input_text}))