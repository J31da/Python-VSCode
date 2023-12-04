#create a simple church age range database (Registration, Database)

#This will get the name, age, gender of the church member

#save this in a database and display on a new page (this page MUST have a login feature)

#Make sure you group members in different category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )
# save all information in a csv file

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = ['Registration', 'Database']
choice = st.sidebar.selectbox('Menu',menu)

df = pd.read_csv('tofechurch.csv')

if choice == 'Database':
    st.sidebar.subheader('Log In To See Database')
    corrpass = '4Pass'
    sp1,sp2 = st.columns(2)
    with sp1:
        passw = st.sidebar.text_input("Enter Password",type='password')
        passbutt = st.sidebar.button("Login")
    if passbutt:
        if passw:
            if passw == corrpass:
                st.dataframe(df,use_container_width=True)
            else:
                st.sidebar.error("Incorrect Password!")

        else:
            st.sidebar.error("Input Password!")

if choice == 'Registration':
    st.subheader("Register For Classes")
    st.divider()

    Nname,Aage = st.columns(2)  
    with Nname:
        name = st.text_input("Enter Your Name")
    with Aage:
        age = st.number_input("Enter Your Age",0)
    Ggender,sp3 = st.columns(2)
    with Ggender:
        gender = st.selectbox(
            'Gender',
            ('Male', 'Female'))
        
    if age < 13 and age >= 3:
        church_class = "Kids"
    elif age <= 19 and age >= 13:
        church_class = "Teens"
    elif age <= 35 and age >= 20:
        church_class = "Youth"
    elif age < 65 and age >= 36:
        church_class = "Adult"
    elif age >= 65:
        church_class = "Elders"

    if st.button("Submit Membership Form"):
      if (name and age and gender):
         member_df = pd.DataFrame({'Name':[name], 'Age':[age], 'Gender':[gender], 'Class':[church_class]})
         new_df = pd.concat([df,member_df],ignore_index=True)
         new_df.to_csv('tofechurch.csv',index=False)
         st.success('Form Has Been Registered!')

      else:
         st.error('Please Fill In All Boxes')