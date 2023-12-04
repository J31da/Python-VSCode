'''
Savings

Save Now
-New week Date - To choose new start date of the week st.date_input(‘Enter the first date”)
-Monday savings- Enter monday savings (use 2 columns for 2 days)
Continue all the way to sunday
Use a submit button to save into csv file

CSV file
Days | Amount | Total Saved 



View Savings (database )
This shows everything in the CSV file
'''
import streamlit as st
import pandas as pd

df = pd.read_csv('test_save.csv')
st.subheader("Savings Of The Week")


mon,tue = st.columns(2)
with mon:
    choose_mon = st.date_input("Enter Monday's Date: ")
    mon_save = st.number_input("Enter Monday's Savings: ")
with tue:
    choose_tue = st.date_input("Enter Tuesday's Date: ")
    tue_save = st.number_input("Enter Tuesday's Savings: ")

st.divider()

wed,thu = st.columns(2)
with wed:
    choose_wed = st.date_input("Enter Wednesday's Date: ")
    wed_save = st.number_input("Enter Wednesday's Savings: ")
with thu:
    choose_thu = st.date_input("Enter Thursday's Date: ")
    thu_save = st.number_input("Enter Thursday's Savings: ")

st.divider()

fri,sat = st.columns(2)
with fri:
    choose_fri = st.date_input("Enter Friday's Date: ")
    fri_save = st.number_input("Enter Friday's Savings: ")
with sat:
    choose_sat = st.date_input("Enter Saturday's Date: ")
    sat_save = st.number_input("Enter Saturday's Savings: ")

st.divider()

choose_sun = st.date_input("Enter Sunday's Date: ")
sun_save = st.number_input("Enter Sunday's Savings: ")

if st.button("Submit Savings Per Week"):
    save_df = pd.DataFrame({"Monday's Date":[choose_mon], "Monday's Savings":[mon_save], "Tuesday's Date":[choose_tue], "Tuesday's Savings":[tue_save],
                            "Wednesday's Date":[choose_wed], "Wednesday's Savings":[wed_save], "Thursday's Date":[choose_thu], "Thursday's Savings":[thu_save],
                            "Friday's Date":[choose_fri], "Friday's Savings":[fri_save], "Saturday's Date":[choose_sat], "Saturday's Savings":[sat_save],
                            "Sunday's Date":[choose_sun], "Sunday's Savings":[sun_save]})
    new_df = pd.concat([df,save_df],ignore_index=True)
    new_df.to_csv('test_save.csv',index=False)
    st.success("Saved!")

st.write("")
st.divider()
st.write("")

st.dataframe(df,use_container_width=True)