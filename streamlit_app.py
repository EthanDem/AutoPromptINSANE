import streamlit as st
import requests



url = "https://test-auto-prompt-select.icecube1513.repl.co/request"

userC = st.text_input("Enter Website Here")

userQ = st.text_input("Enter Query Here")

data = {
    "query":userQ,
    "content": userC
}

if st.button("Submit"):

  response = requests.post(url, json=data)
  
  st.write("Status Code:", response.status_code)
