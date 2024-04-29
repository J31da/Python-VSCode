import streamlit as st
import pandas as pd
import plotly.express as px
import time

st.set_page_config(layout='wide')

st.subheader('**csv charter**')
st.divider()

timestamp = int(time.time())
cl1,cl2 = st.columns([0.3,0.2])

with cl1:
    upload = st.file_uploader('upload csv file',type=['csv'])

    st.divider()
    st.write('')
    if upload:
      csv_file = pd.read_csv(upload)
      st.write(csv_file)
  
    csv_list = csv_file['title'].to_list()
    sub = st.multiselect(
         'subjects to plot',
         (csv_file))
    
    st.write('')
    st.divider()

    st.subheader('chart type')
    st.subheader('')
    
    ct1,ct2 = st.columns(2)

    with ct1:
      chartype = st.selectbox(
           'type of chart',
           ('bar chart', 'pie chart'))
      st.write('')
      st.write('')

      st.divider()
      if chartype == 'bar chart':
           sub_score = csv_file[sub].mean().reset_index()
           sub_new = sub_score.rename(columns={'index':'Grade', 0:'Total'})

           barchart = px.bar(sub_new, x = 'Subjects', y ='Average')
           st.plotly_chart(barchart)
     
      if chartype == 'pie chart':
            sub_count = csv_file['Total'].value_counts().reset_index
            #st.write(sub_count)

           #grade_counts = df['Grade' ].value_counts().reset_index()
           #st.write(grade_counts)


            piechart = px.pie(sub_count,names='Name',values='Total')
            st.plotly_chart(piechart)
