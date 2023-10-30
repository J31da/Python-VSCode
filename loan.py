import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

menu = ['Register Loan','Loan Database']
choice = st.sidebar.selectbox('Menu',menu)

df = pd.read_csv('loans.csv')
loan_id = 'LOANER' + str(len(df) + 1)

if choice == 'Loan Database':
    st.dataframe(df,use_container_width=True)

if choice == 'Register Loan':
    st.subheader("Loan Application Form")
    st.write("Please fill in all required information in the loan application form below \
             to request a loan from your organisation. Information requiring income assets \
             are required for qualification.")
    st.divider()

    loanamount = st.number_input("Desired loan amount")
    annualincome = st.number_input("Annual Income")
    loanuse = st.selectbox(
        'Loan Use',
        ('Business','Health Home', 'Purchase', 'Home Renovation', 'Education', 'Traveling', 'Vacation', 'Relocation')) 
    fn,ln = st.columns(2)
    with fn:
        name = st.text_input("First Name: ")
    with ln:
        name2 = st.text_input("Last Name: ")

    bday = st.date_input("Birth Date")

    pn,ml = st.columns(2)
    with pn:
     phonenum = st.text_input("Phone number: ")
    with ml:
     mail = st.text_input("Email: ")
    address = st.text_input("Address: ")

    df = pd.read_csv('loans.csv')


    if st.button("Submit Loan Application"):
        if (name and name2 and loanamount and loanuse and annualincome and bday and phonenum and mail and address):
                loan_df = pd.DataFrame({'Loan ID': [loan_id], 'First Name':[name],'Last Name':[name2], 'Loan Amount':[loanamount], 'Loan Use':[loanuse], 'Annual Income':[annualincome], 'Birth Date':[bday], 'Phone Number':[phonenum], 'Mail':[mail], 'Address':[address]})
                new_df = pd.concat([df,loan_df],ignore_index=True)
                new_df.to_csv('loans.csv',index=False)
                st.success('Loan Data Saved')
        else :
            st.error('Kindly Fill All The Boxes')