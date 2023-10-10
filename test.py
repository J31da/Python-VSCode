# Test:
# Create a simple and short web page that
# -Ask for student name on the left column and their age on the right column
# -create a button
# -save this in a csv file
# show it on top of the page (dont create a new page)

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df = pd.read_csv('testdatabase.csv')
st.dataframe(df,use_container_width=True)

with st.form(key='Test',clear_on_submit=True):
    st.title('Test')

    name,age = st.columns(2)

    with name:
        fn = st.text_input("First Name")
        ln = st.text_input("Last Name")

    with age:
        ageselect = st.text_input("Age")
        yeargroup = st.text_input("Year Group")



    def add_students(fn,ln,ageselect,yeargroup,df):
     students_dict = {'Student First Name':fn,'Student Last Name':ln,'Age':ageselect,'Year Group':yeargroup}
     students_df = pd.DataFrame([students_dict]) 
     df = pd.concat([df,students_df],ignore_index=True) 
     return df


    if st.form_submit_button('Submit'):
         df = add_students(fn,ln,ageselect,yeargroup,df)
         df.to_csv('testdatabase.csv',index=False)
    
