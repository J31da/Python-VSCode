import streamlit as st
import pandas as pd
import time

st.set_page_config(layout='wide')

st.subheader('**csv editor**')
st.divider()

timestamp = int(time.time())
col1,col2 = st.columns(2)

with col1:
 upload = st.file_uploader("upload csv file",type=['csv'])

 st.divider()
 st.write('')

if upload:
   csv_file = pd.read_csv(upload)
   edit_csv = st.data_editor(csv_file,use_container_width=True)

sav1,sav2,space = st.columns([1,1,4])
with sav1:
   if st.button('save as original file'):
      edit_csv.to_csv(upload.name,index=False)
      st.success('original csv file saved')

with sav2:
   if st.button('save as copy'):
      new_filename = f'{upload.name}_{timestamp}.csv'
      csv_copy = edit_csv.to_csv(new_filename,index=False)
      st.success('csv file copy saved')