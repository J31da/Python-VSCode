#create a simple church age range database
#This will get the name, age, gender of the church memeber
#save this in a database and display on a new page (this page MUST have a login feature)
#Group members in differnt category based on their age 
# (Kids(3 - 12), Teens, Youth(13-19), Adult(20-64), Elders(65+) )

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = ['Register Member', 'Member Database']
choice = st.sidebar.selectbox('Menu',menu)

df = pd.read_csv('churchage.csv')

if choice == 'Member Database':
   st.sidebar.subheader('Log In To View Members')
   correctpass = 'Jeida123'
   space1,space2 = st.sidebar.columns(2)
   with space1:
       passw = st.sidebar.text_input("Enter Password", type='password')
       passbutt = st.sidebar.button("Login")
   if passbutt:
     if passw:
          if passw == correctpass:
             st.dataframe(df,use_container_width=True)
          else:
             st.sidebar.error("Wrong Password!")

     else:
       st.sidebar.error("Input Password!")

if choice == 'Register Member':
   st.subheader("Register For Classes")
   st.divider()

   Nname,Age = st.columns(2)
   with Nname:
      name = st.text_input("Enter Your Name")
   with Age:
      age = st.number_input("Enter Your Age",0)
   Gen,space3 = st.columns(2)
   with Gen:
      gender = st.selectbox(
         'Gender',
         ('Male','Female'))
   
   if age < 13 and age >= 3:
      church_class = 'Kids'
   elif age <= 19 and age >= 13:
      church_class = 'Teens'
   elif age < 65 and age >= 20:
      church_class = 'Adult'
   elif age >= 65:
      church_class = 'Elders'
    
   if st.button("Submit Membership Application"):
      if (name and age and gender):
         member_df = pd.DataFrame({'Name':[name], 'Age':[age], 'Gender':[gender], 'Class':[church_class]})
         new_df = pd.concat([df,member_df],ignore_index=True)
         new_df.to_csv('churchage.csv',index=False)
         st.success('Application Has Been Registered!')

      else:
         st.error('Please Fill In All Boxes')