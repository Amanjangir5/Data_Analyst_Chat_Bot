from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import warnings


warnings.filterwarnings("ignore")

load_dotenv()
API_KEY = os.environ['OPENAI_API_KEY']

llm = OpenAI(api_token=API_KEY)
pandas_ai = PandasAI(llm)


st.title('Panda Analyst')
uploaded_file = st.file_uploader('Upload a CSV file',type=['csv','xlsx'])

if uploaded_file is not None:

    # Check the file extension
    file_extension = uploaded_file.name.split('.')[-1]

    if file_extension == 'csv':
        df = pd.read_csv(uploaded_file)
    elif file_extension in ['xls', 'xlsx']:
        df = pd.read_excel(uploaded_file)
    else:
        st.error('Unsupported file format. Please upload a CSV or Excel file.')
        st.stop()  # Stop execution if an unsupported file format is uploaded
    
    st.write(df.head(3))

    prompt = st.text_area('Enter your prompt: ')

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating responce..."):
                st.write(pandas_ai.run(df,prompt=prompt))
        else:
            st.warning("Please enter your prompt")