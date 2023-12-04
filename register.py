import streamlit as st
import pandas as pd


menu = st.sidebar.selectbox('menu', ['Register', 'Login'])

if menu == 'Register':
    userdetails = st.sidebar.container()
    with userdetails:
      username = st.sidebar.text_input('Enter your username',value='')
      password = st.sidebar.text_input("Enter your password", type= 'password',value='')
      passwordcheck = st.sidebar.text_input("Enter your password again", type= 'password',value='')
      submit = st.sidebar.button('Register')

    if submit:
      if username and password and passwordcheck:
         if password == passwordcheck:
             userdetails.empty()
             st.title('Hello you are in')

         else:
             st.sidebar.error("Password do not match")

      else:
          st.sidebar.error("Kindly Fill In All Boxes")

if menu == 'Login':
    st.session_state
    loginusername = st.sidebar.text_input('Enter your username', value='')
    loginpassword = st.sidebar.text_input("Enter your password", type='password', value='')
    submit = st.sidebar.button('Register')
    if submit:
        if loginusername and loginpassword:
            if loginusername == username and loginpassword == password:
                userdetails.empty()
                st.title('Hello you are in ')
            else:
                st.sidebar.error("Password do not match")
        else:
            st.sidebar.error("Kindly Fill In All Boxes")