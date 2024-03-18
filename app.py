#Creating the chatbot
#Q&A Chatbot

from langchain.llms import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv() # Take environment variables from .en

## Function to load OPENAI Modela dn get response

def get_openai_response(question:str):

    #Initializing the LLM Model
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)

    #Getting the response
    response = llm(question)

    #Return the response
    return response

##Initialize the Streamlit App

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input:- ", key="input")
response = get_openai_response(input)

submit=st.button("Ask the question!")

#If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)