import streamlit_scrollable_textbox as stx
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = ['register','login']
choice = st.sidebar.selectbox('menu',menu)

df = pd.read_csv('journal.csv')

if choice == 'register':
    regusern = st.sidebar.text_input('enter your username',value='') 
    regpass = st.sidebar.text_input('enter your password',value='',type='password')
    regpasscheck = st.sidebar.text_input('enter your password again',value='',type='password')
    submit = st.sidebar.button('register')
    if submit:
        if regusern and regpass and regpasscheck:
            if regpass == regpasscheck:
                loginregdf = pd.DataFrame({'username':[regusern],'password':[regpass]})
                new_df = pd.concat([df,loginregdf],ignore_index=True)
                new_df.to_csv('journal.csv',index=False)

                st.sidebar.success('successfully registered! please login')
            else:
                st.sidebar.warning('passwords do not match')
        else:
            st.sidebar.error('kindly fill all text-boxes')
if choice == 'login':
    pas1,pas2 = st.sidebar.columns(2)
    col1,col2 = st.columns(2)
    with pas1:
        usern = st.sidebar.text_input('enter username',value='')
        passw = st.sidebar.text_input('enter password',value='',type='password')
        passb = st.sidebar.button('login')

        if passb:
            if passw and usern:
                find_result = df[df['username'] == usern]
                corrpass = find_result['password'].iloc[0]
                if passw == corrpass:
                    st.sidebar.success('logged in!')
                    with col1:
                     st.subheader(f':blue[**logged in {usern}!**]')
                     st.divider()
                     st.header("")
                     st.subheader("secrets:")
                     st.write("")
                     paragraph = stx.scrollableTextbox('')
                     notes = st.text_input('enter your notes: ')

                     st.write("")
                     if st.button('Save'):
                         loginregdf = pd.DataFrame({'notes':[notes]})
                         new_df = pd.concat([df,loginregdf],ignore_index=True)
                         new_df.to_csv('journal.csv',index=False)

                         st.sidebar.success('saved!')
                         
                         find_result = df[df['password'] == passw ]
                         getfn = find_result['notes'].iloc[0]
                         paragraph = getfn
                     
                else:
                    st.sidebar.warning('username and password do not match')
            else:
                st.sidebar.error('kindly fill all text-boxes')
