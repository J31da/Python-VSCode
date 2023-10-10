import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df = pd.read_csv('grades.csv')
st.dataframe(df,use_container_width=True)

