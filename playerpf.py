import streamlit as st
import pandas as pd
import plotly.express as px
import time

st.set_page_config(layout='wide')

st.subheader('**Player Performance Data**')
st.divider()
st.write('')

player = pd.read_csv('player_performance.csv')

ft1,ft2,ft3 = st.columns([0.1,0.1,0.1])
ft4,ft5 = st.columns(2)

with ft4:
    playernm = st.text_input("Enter player's name: ")

with ft1:
    goals = st.number_input(':blue[**Number of goals scored by the player:**]',value=0)
    
    assists = st.number_input(':white[**Number of assists made by the player**]',value=0)

with ft3:
    tackles = st.number_input(':white[**Number of tackles made by the player:**]',value=0)

    passes = st.number_input(':blue[**Number of passes made by the player:**]',value=0)


st.write('')

if st.button('Save Data'):
    plydict = {'Player Name':[playernm],'Goals':[goals],'Assists':[assists],'Tackles':[tackles],'Passes':[passes]}
    ply_df = pd.DataFrame(plydict)
    plyjoin = pd.concat([player,ply_df],ignore_index=True)
    plyjoin.to_csv('player_performance.csv',index=False)

    st.success('Saved!')


st.divider()
st.write('')

st.subheader('**View Player Stats:**')
st.subheader('')
 
st1,st2 = st.columns([0.5,0.5])
# stat = player.columns.tolist()
stat = ['Goals','Assists','Tackles','Passes']

with st1:
    stat_choice = st.radio('Stats To Plot',stat,horizontal=True)
    st.subheader('')

rows = 4
st.table(player.head(rows))

if stat_choice == 'Assists':
    assichart = px.line(player, x ='Player Name', y ='Assists')
    st.plotly_chart(assichart)

if stat_choice == 'Tackles':
    tachart = px.line(player, x ='Player Name', y ='Tackles')
    st.plotly_chart(tachart)

if stat_choice == 'Passes':
    pachart = px.line(player, x ='Player Name', y ='Passes')
    st.plotly_chart(pachart)

if stat_choice == 'Goals':
    glchart = px.line(player, x ='Player Name', y ='Goals')
    st.plotly_chart(glchart)