import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.subheader('**csv editor**')
st.divider()

col1,col2 = st.columns(2)

with col1:
 upload = st.file_uploader("upload csv file",type=['csv'])

 st.divider()
 st.write('')

if upload:
   csv_file = pd.read_csv(upload)
   edit_csv = st.data_editor(csv_file,use_container_width=True)

if st.button('save edited csv'):
    st.success('csv file saved')
    edit_csv.to_csv(upload.name,index=False)

if st.button('save as'):
   st.success('csv file saved')
   edit_csv.to_csv(upload,index=False)