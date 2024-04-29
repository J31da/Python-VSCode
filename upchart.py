import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

st.subheader('**data charter**')
st.divider()

up1,up2 = st.columns([0.3,0.2])

with up1:
    upload_csv = st.file_uploader('upload csv file',type='csv')
    st.divider()
    st.write('')

if upload_csv:
    csv_file = pd.read_csv(upload_csv)
   
    with st.expander('view database'):
     st.table(csv_file)
    
    sub = csv_file.columns.tolist()
    sub_choice = st.multiselect('subjects to plot',sub)
    
    sub_avg = csv_file[sub_choice].mean().reset_index()
    rename_sub = sub_avg.rename(columns = {'index':'subject', 0:'average'})

    ct1,ct2 = st.columns(2)

    with ct1:  
        st.divider()
        st.write('')
        chartype = st.radio('Type of chart',['bar chart', 'pie chart'],horizontal=True)
        st.write('')
        st.write('')

        st.divider()
        if chartype == 'bar chart':
            barchart = px.bar(rename_sub, x = 'subject', y = 'average')
            st.plotly_chart(barchart)
        
        if chartype == 'pie chart':
            piechart = px.pie(rename_sub, names = 'subject', values = 'average')
            st.plotly_chart(piechart)