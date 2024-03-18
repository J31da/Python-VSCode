import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('select option',['create note', 'view notes', 'update notes'])

notes = pd.read_csv('notes.csv')
if menu == 'create note':
    bd1,bd2,bd3 = st.columns([0.2,4,0.2])

    with bd2:
        with st.form('notes form',clear_on_submit=True):
            st.header(':red[**create a new note**]')
            st.divider()
            
            nt1,nt2 = st.columns(2)
        
            with nt1:
                notitle = st.text_input('enter the title for your new note: ')
            with nt2:
                notedate = st.date_input('select the note date: ')

            notecontent = st.text_area('enter your new notes: ',height=250)
            
            sv1,sv2 = st.columns(2)
            
            with sv1:
             if st.form_submit_button('save note'):
                 if notitle and notecontent:
                     notedict = {'title':[notitle],'dates':[notedate],'note content':[notecontent]}
                     note_df = pd.DataFrame(notedict)
                     notejoin = pd.conacat(notes,note_df)
                     notejoin.to_csv('notes.csv')

                     st.success('note saved succesfully!')
            
elif notes == 'view notes':
    