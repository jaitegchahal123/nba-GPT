import os
import sys
import math
import constants
import time
import pandas as pd
import requests

from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate



os.environ["OPENAI_API_KEY"] = st.secrets["openai_secret_key"]

# Display the text in the upper corner
st.markdown(
    """
    <div style="position: absolute; top: 10px; right: 10px; font-size: 14px; font-weight: bold;">
    Made by Jaiteg Chahal
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.text("Jaiteg Chahal")

st.sidebar.markdown('[LinkedIn](https://www.linkedin.com/in/jaiteg-chahal/)', unsafe_allow_html=True)
st.sidebar.markdown('[Github](https://github.com/jaitegchahal123)', unsafe_allow_html=True)
st.sidebar.text("jchahal@berkeley.edu")
# Add a horizontal line using HTML tags
st.sidebar.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

st.sidebar.markdown("<hr>", unsafe_allow_html=True)

# Add the "published" text at the top
st.sidebar.write("Published 07/07/2023")
# st.sidebar.text("published 07/07/2023")



            
st.title('🏀 NBA GPT | 2022-2023 NBA Season')
prompt = st.text_input('Type in your prompt here')

query = "Give me ALL the info you know about this. Even if you don't know much, expand on what you do know and go in depth:" + prompt


#downloads_path = os.path.expanduser("~/Desktop/dataVU")
# Create a DirectoryLoader with the Downloads folder and "*.txt" as the glob pattern
#loader = DirectoryLoader(downloads_path, glob="*.json")


llm = OpenAI(temperature=0.9)
loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])


#print(index.query(query, llm=ChatOpenAI()))
if prompt:
    #response = llm(prompt)
    st.write(index.query(query, llm=ChatOpenAI()))

# #loader = DirectoryLoader('.', glob="x.txt")




