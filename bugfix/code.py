import streamlit as st
import base64
import openai

openai.api_key = "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"

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

st.title("BugFix")
ques =st.text_area("Enter a Question")
codetxt="""
##### Fix bugs in the below function

### Buggy Python
{}
### Fixed Python
        """.format(ques)
if st.button('Fix'):     
    response = openai.Completion.create(
            engine="davinci-codex",
            prompt=codetxt,
            temperature=0,
            max_tokens=200,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0.0,
            stop=["#"]
            )
    ans=response['choices'][0]['text']
    st.code(ans, language="python")

