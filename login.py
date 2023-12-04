import streamlit as st
import pandas as pd

st.sidebar.subheader('Login to see my page')
correctpassword= 'Jeida'
pass1, pass2 = st.sidebar.columns(2)
with pass1:
 password = st.sidebar.text_input("Enter the school password", type='password')
 database = pd.read_csv('employee.csv')
 passwordbutton = st.sidebar.button("Login")
if passwordbutton:
 if password:
     if password == correctpassword:
         st.dataframe(database, use_container_width=True)
     else:
         st.sidebar.error("Error! Wrong password")
        
else:
    st.sidebar.error('Input Password!')