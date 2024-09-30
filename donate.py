import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('Select Option',['Create Donation', 'View Donations', 'Donate'])

donate = pd.read_csv('donate.csv')

if menu == 'Create Donation':
    bd1,bd2,bd3 = st.columns([0.2,4,0.2])

    with bd2:
        with st.form('create donation form',clear_on_submit=True):
            st.header(':blue[**Create Donation**]')
            st.divider()
            
            dn1,dn2 = st.columns(2)
            with dn1:
             dntitle = st.text_input('Campaign Title')

            em1,em2 = st.columns(2)
            with em1:
               em = st.text_input('Email')

            st.divider()

            dsc1,dsc2 = st.columns([3.2,1])
            with dsc1:
             dsc = st.text_area('Campaign Details',height=50)

            am1,am2 = st.columns(2)
            with am1:
               goalam = st.selectbox(
            ':blue[**Goal Amount**]',
            ('$50', '$100', '$150', '$200', '$250', '$300', '$350', '$400', '$450', '$500'))

            cr1,cr2 = st.columns(2)

            with cr1:
               if st.form_submit_button('Create'):
                if dntitle and em and dsc:
                   dndict = {'Title':[dntitle],'Email':[em],'Campaign Details':[dsc],'Goal Amount':[goalam]}
                   dn_df = pd.DataFrame(dndict)
                   dnjoin = pd.concat([donate,dn_df],ignore_index=True)
                   dnjoin.to_csv('donate.csv',index=False)

                   st.success('Created!')
                else:
                   st.error('Fill In All Boxes')

if menu == 'View Donations':

   st.header(':blue[**View Donations**]')
   st.divider()

   dnttitle = donate['Title'].to_list()
   dnt1,dnt2 = st.columns([0.3,0.4])

   with dnt1:
      slctitle = st.selectbox('Select Donation To View',dnttitle)

   filter_title = donate[donate['Title'] == slctitle]
   content = filter_title['Campaign Details'].iloc[0]
   mail = filter_title['Email'].iloc[0]
   space = ''

   st.divider()

   st.write(space)
   dnte1,dnte2 = st.columns([0.3,0.3])

   with dnte1:
      st.subheader('Campaign Details')
   with dnte2:
      gamount = filter_title['Goal Amount'].iloc[0]
      st.subheader(f':blue[**Goal Amount: {gamount}**]')
       
   st.divider()
   st.write(space)
   st.write(content)

   st.write(f':blue[**Contact us at: {mail}**]')


if menu == 'Donate':

   st.header(':blue[**Select Donation**]')
   st.divider()

   dntt = donate['Title'].to_list()
   dnta1,dnta2 = st.columns([0.3,0.3])

   with dnta1:
      slcdn = st.selectbox('Select Donation',dntt)

   st.divider()
   st.write('')

   dnam1,dnam2 = st.columns([0.18,0.3])

   with dnam1:
    dn = st.number_input('Enter Donation Amount: ',step=25,value=0)
    if st.button('Donate'):
         st.success('Donated! Thank You For Contributing To Our Cause.')

   