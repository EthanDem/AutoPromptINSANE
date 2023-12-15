import streamlit as st
import requests


st.set_page_config(page_title="INSANE", page_icon=":shushing_face:")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {
    visibility: hidden;
}
footer:after {
    content: 'made by nBrain';
    visibility: visible;
    display: block;
    position: relative;
    /* background-color: red; */
    padding: 5px;
    top: 2px;
}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

url = "https://auto-prompt.icecube1513.repl.co/request"

userC = st.text_input("Enter Website Here")

userQ = st.text_input("Enter Query Here")

data = {
    "query":userQ,
    "content": userC
}

if st.button("Submit"):

    response = requests.post(url, json=data)
    
    parsed_response = response.json()
    
    messages = parsed_response['message']

    for msg in messages:
        st.write(msg)
