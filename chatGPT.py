import os
import sys
import pandas as pd
import requests
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
import streamlit as st


# Gets OPEN_AI API key.
os.environ["OPENAI_API_KEY"] = st.secrets["openai_secret_key"]

# Add the title            
st.title('🏀 NBA GPT | 2022-2023 NBA Season')

# Display the text in the upper corner
st.markdown(
    """
    <div style="position: absolute; top: 10px; right: 10px; font-size: 14px; font-weight: bold;">
    Made by Jaiteg Chahal
    </div>
    """,
    unsafe_allow_html=True
)

# Add information sidebar.
st.sidebar.text("Jaiteg Chahal")
st.sidebar.markdown('[LinkedIn](https://www.linkedin.com/in/jaiteg-chahal/)', unsafe_allow_html=True)
st.sidebar.markdown('[Github](https://github.com/jaitegchahal123)', unsafe_allow_html=True)
st.sidebar.text("jchahal@berkeley.edu")

# Add a horizontal line using HTML tags
st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Add the "published" text at the bottom
st.sidebar.write("Published 07/07/2023")

# Text above prompt bar.
prompt = st.text_input('Type in your prompt here')

# This is the query that chat-gpt will answer. Custom prompt + whatever the user types in as {prompt}.
query = "Give me ALL the info you know about this. Even if you don't know much, expand on what you do know and go in depth:" + prompt

# Create the llm and load data from .txt file.
llm = OpenAI(temperature=0.9)
loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

# To pass in more than one file:
    # loader = DirectoryLoader('.', glob="x.txt")

# Given a prompt, pass our query into the llm.
if prompt:
    st.write(index.query(query, llm=ChatOpenAI()))