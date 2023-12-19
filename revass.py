'''
Class Assessment
----------------------------
'''
import streamlit as st
import pandas as pd

#1) What is Streamlit used for?
#- helps use framework for python program

#2) Show 8 ways to display text on Streamlit?
one = st.write('hi') 
two = st.text_input('enter name') 
three = st.number_input('enter age',value=0)
four = st.success('correct')
five = st.error('wrong') 
six = st.button('click me')
seven = st.subheader('seven') 
eight = st.header('eight')
st.divider()
st.subheader("")

#3) Show how to ask for a text on Streamlit:
text = st.text_input("enter text")
st.divider()

#4) Show how to ask for a number on Streamlit:
number = st.number_input("enter number",value=0)
st.divider()
st.subheader("")

# 5) Create a button on the left column but show the output on the right column
butt,out = st.columns(2)

with butt:
    if st.button('click'):
        st.write('-----------)))')
with out:
    st.write('done')
st.divider()
st.subheader("")

#6.create a radio button with a horizontal orientation
pet = st.radio(':blue[**pets**]',['dog', 'cat', 'other/none'],horizontal=True)
st.divider()
st.subheader("")

#7.import an image with a 150*150 size
dog = st.image('https://dogtime.com/wp-content/uploads/sites/12/2011/01/GettyImages-997016774-e1694111248101.jpg?w=1024',width=150)
st.divider()
st.subheader("")

#8. read and dispay a CSV file in python
df = pd.read_csv('loans.csv')
st.dataframe(df,use_container_width=True)
st.divider()
st.subheader("")

#9.create a toggle option to display any database/dataframe
menu = ['main page','database']
choice = st.sidebar.selectbox('menu',menu)

if choice == 'main page':
    st.subheader('**main page**')
    st.divider()
if choice == 'database':
    st.subheader('**database**')
    st.divider()
    st.subheader('')
    st.dataframe(df,use_container_width=True)
st.divider()
st.subheader("")


#10.create a dictionary of 5 different cars with 5 attributes (without using a CSV file)
#and convert it to a dataframe/table

dict = {
    'Mercedes' : ['$800,450', 'grey', '1985', 'used', '5 year insurance'],
    'Ferrari' : ['$983,900', 'red', '2010', 'used', '1 year insurance'],
    'Buggati' : ['$9,830,900', 'black', '2022', 'unused', '3 year insurance'],
    'Rolls-Royce' : ['$980,700', 'platinum', '2020', 'used', '10 month insurance'],
    'Lexus' : ['$799,080', 'gold', '2023', 'unsused', '2 year insurance']
}

dict_df = pd.DataFrame(dict)
st.dataframe(dict_df,use_container_width=True)