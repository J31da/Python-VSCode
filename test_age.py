'''
Test:
Create a simple python program that
-create a menu for student details and students database
-Ask for student name on the left column and their age on the right column
-create a submit button
- save this in a csv file
- show the dataframe in database page
'''
import streamlit as st
import pandas as pd

menu = ['Register Student Details', 'Student Database']
choice = st.sidebar.selectbox('Menu',menu)

df = pd.read_csv('test_age.csv')

if choice == 'Student Database':
    st.dataframe(df,use_container_width=True)

if choice == 'Register Student Details':
    st.subheader("Fill In Details")
    st.divider()
    st.write("")
    fn,ages = st.columns(2)
    with fn:
        fulln = st.text_input("Please Enter Your Full Name: ")
    with ages:
        age = st.text_input("Please Enter Your Current Age: ")
    st.write("")

    df = pd.read_csv('test_age.csv')

    if st.button("Submit Details"):
        stud_df = pd.DataFrame({'Name':[fulln], 'Age':[age]})
        new_df = pd.concat([df,stud_df],ignore_index=True)
        new_df.to_csv('test_age.csv',index=False)
        st.success("Succesfully Saved!")