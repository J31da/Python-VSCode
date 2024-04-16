import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('select option',['create recipe', 'view recipes', 'update recipe'])

notes = pd.read_csv('recipes.csv')
if menu == 'create recipe':
    bd1,bd2,bd3 = st.columns([0.2,4,0.2])

    with bd2:
        with st.form('create recipe form',clear_on_submit=True):
            st.header(':green[**create recipe**]')
            st.divider()
            
            nt1,nt2 = st.columns(2)
        
            with nt1:
                notitle = st.text_input('enter the title for your new recipe: ')
            with nt2:
                notedate = st.date_input('select the recipe date: ')

            notecontent = st.text_area('enter your new recipe: ',height=220)
            
            sv1,sv2 = st.columns(2)
            
            with sv1:
             if st.form_submit_button('save recipe'):
                 if notitle and notecontent:
                     notedict = {'title':[notitle],'dates':[notedate],'recipe content':[notecontent]}
                     note_df = pd.DataFrame(notedict)
                     notejoin = pd.concat([notes,note_df],ignore_index=True)
                     notejoin.to_csv('recipes.csv',index=False)
                     
                     st.success('succesfully saved!')
            
elif menu == 'view recipes':
    st.header(':green[**view recipes**]')
    st.divider()

    note_title = notes['title'].to_list()
    nt1,nt2 = st.columns([0.4,0.2])

    with nt1:
     select_title = st.selectbox('select recipe to view',note_title)
    
    filter_title = notes[notes['title'] == select_title]
    # st.table(filter_title)
    content = filter_title['recipe content'].iloc[0]
    space = ''

    st.divider()


    st.write(space)
    nc1,nc2 = st.columns([0.3,0.3])

    with nc1:
       st.subheader(f':green[**selected recipe content:**]')
    with nc2:
       date = filter_title['dates'].iloc[0]
       st.subheader(f':green[**recipe date: {date}**]')
       
    st.divider()
    st.write(space)
    st.write(content)

elif menu == 'update recipe':
   st.header(':green[**update recipes**]')
   st.divider()

   note_title = notes['title'].to_list()
   nt1,nt2 = st.columns([0.4,0.2])

   with nt1:
     select_title = st.selectbox('select recipe to update',note_title)
   
   st.write('')
   st.divider()

   filter_title = notes[notes['title'] == select_title]
   content = filter_title['recipe content'].iloc[0]

   upd1,upd2 = st.columns([0.5,0.2])

   with upd1:
     update_note = st.text_area('edit recipe',content,350)

   if st.button('save edits'):
      notes.loc[notes['title'] == select_title, 'recipe content'] = update_note
      notes.to_csv('recipe.csv',index=False)
      
      ed1,ed2 = st.columns([0.3,0.3])
      with ed1:
         st.success('successfuly edited!')
