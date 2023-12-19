import streamlit as st
import pandas as pd

st.sidebar.subheader("Login to see my page")
csvlink = pd.read_csv('nwlogin.csv')

corrpass = csvlink['password'].iloc[0]

pass1, pass2 = st.sidebar.columns(2)
with pass1:
    passw = st.sidebar.text_input('Enter password', type='password')
    passbutt = st.sidebar.button('Login')
    if passbutt:
     if passw:
        if passw == corrpass:
           st.dataframe(csvlink, use_container_width=True)
        else:
           st.sidebar.error('Error! Incorrect Password')
     else:
        st.sidebar.error('Input Password!')

