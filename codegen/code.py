import requests
import streamlit as st
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
       data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
        <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
        ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('background.png')

st.title("Code Generator")
ques =st.text_input("Enter a Question")
promptxt="""
--
Q: Write a Python program that calculates the sum of all positive integers smaller than 8.
A: sum(x for x in range(8))
--
Q: {}
A:
""".format(ques)
response = requests.post(
    "https://api.ai21.com/studio/v1/j1-jumbo/complete", # models- j1-large, j1-jumbo
    headers={"Authorization": "Bearer tADwpGNrHnbOtI8OhPPmzyZxiOwrXGsx "},
    json={
        "prompt": promptxt, 
        "numResults": 1, 
        "maxTokens": 200, 
        "stopSequences": ["--"], #where it should it end
        "topKReturn": 0,
        "temperature": 0.0
    }
)
resp=response.json()
ans=resp['completions'][0]['data']['text']
st.code(ans, language="python")

