import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout='wide')
st.title('Student Scores Database')

df = pd.read_csv('codingscores.csv')
rows = 6

st.table(df.head(rows))

reduce,increase = st.columns(2)

with increase:
 if st.button('Show More Scores:'):
     rows += 5

with reduce:
   if st.button('Show Less Scores:'):
      rows -= 5


st.divider()
st.write('')

sub = ['Python','Sql','ML','Tableau','Excel']
sub_score = df[sub].mean().reset_index()
sub_new = sub_score.rename(columns={'index':'Subjects', 0:'Average'})

barchart = px.bar(sub_new, x = 'Subjects', y ='Average')
st.plotly_chart(barchart)

 