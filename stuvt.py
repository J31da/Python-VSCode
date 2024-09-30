import streamlit as st
import pandas as pd
import plotly.express as px
import time

st.set_page_config(layout='wide')

vote = pd.read_csv('stvote.csv')

st.subheader('**Student Voting**')
st.divider()
st.write('')

st1,st2 = st.columns([0.3,0.4])

with st1:
    with st.form('create donation form',clear_on_submit=True):
        name = st.text_input('What is your name? ')
        
        st.write('')

        conts = st.selectbox(
            ':blue[**Choose A Contestant**]',
            ('Maya', 'Stewart', 'Kate', 'Bob', 'Martha'))
        
        st.write('')

        if st.form_submit_button('Vote'):
            vtdict = {'Student Name':[name],'Contestor':[conts]}
            vt_df = pd.DataFrame(vtdict)
            vtjoin = pd.concat([vote,vt_df],ignore_index=True)
            vtjoin.to_csv('stvote.csv',index=False)

            st.success('You Have Voted!')

        st.divider()
        st.write('')

        rows = 4
        st.table(vote.head(rows))

with st2:
    ch1,ch2 = st.columns(2)

    with ch1:
        chartype = st.selectbox(
            'Type of Chart',
            ('Bar Chart', 'Pie Chart'))
        st.write('')

    st.write('')

    st.divider()
    if chartype == 'Bar Chart':
        barchart = px.bar(vote, x = 'Contestor')
        st.plotly_chart(barchart)
    
    if chartype == 'Pie Chart':
        piechart = px.pie(vote, names ='Contestor', values ='Student Name')
        st.plotly_chart(piechart)
    

