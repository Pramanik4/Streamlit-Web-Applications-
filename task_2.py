import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.header("""
Exploratory Data Analysis App
### Upload Your CSV File and Data Analysis on the Dataset you have provided will get Displayed
""")

file_uploaded = st.sidebar.file_uploader("Upload Your Input CSV File", type=["csv"])

if file_uploaded is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(file_uploaded)
        return csv

    data = load_csv()
    pr = ProfileReport(data, explorative=True)
    st.header('**Input DataFrame**')
    st.write(data)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)