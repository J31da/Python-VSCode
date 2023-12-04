'''
Create a menu for Registration and Database
Design a blood donation database that can get donor input
-Name -Contact Number (use text)
-Blood group (use radio or selectbox) -Disease/Infection (use radio or selectbox)

-Submit donor details

Next, save these in a csv file and show the database in a Database page in the menu
'''

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = ['Registration', 'Donation Database']
choice = st.sidebar.selectbox('Menu',menu)

df = pd.read_csv('donor.csv')

if choice == 'Donation Database':
    st.dataframe(df,use_container_width=True)

if choice == 'Registration':
    st.subheader(":red[Blood Donation Registration]")
    st.divider()

    nnme,cn = st.columns(2)
    with nnme:
        name = st.text_input(":red[**Name:**]")
    with cn:
        contactnum = st.text_input(":red[**Contact Number:**]")

    bg,illness = st.columns(2)
    with bg:
        blood_group = st.radio(':red[**Select Your Blood Group**]',['A', 'B', 'AB', 'O'])
    with illness:
        ill = st.radio(':red[**Select Illness**]',['Disease', 'Infection', 'None'],horizontal=True)


    if st.button("Submit Donor Details"):
        donor_df = pd.DataFrame({'Name':[name],'Contact Number':[contactnum],'Blood Group':[blood_group],'Type Of Disease':[ill]})
        new_df = pd.concat([df,donor_df],ignore_index=True)
        new_df.to_csv('donor.csv',index=False)
        st.success("Donor Details Saved!")