import streamlit as st

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('BMI Menu', ['Children BMI','Adult BMI'])

if menu == 'Children BMI':
    st.subheader("Height")
    Metre,Inch = st.columns(2)
    with Metre:
        metres = st.number_input("Metres")
    with Inch:
        inch = st.number_input("Inches")
    st.divider()
    st.subheader("Weight")
    Kilogram,Pound = st.columns(2)
    with Kilogram:
        kilogram = st.number_input("Kilogram")
    with Pound:
        pound = st.number_input("Pounds")
    st.divider()
    

    if st.button("Submit"):
        if (metres,inch,kilogram,pound):
         height = metres * metres
         bmi = kilogram / metres
         if bmi < 18.5:
             bmi_indicator1 = "BMI is underweight"
             st.info(f"Oh no, your {bmi_indicator1}. Your BMI is {bmi}")
         elif bmi >= 18.5 and bmi < 25:
             bmi_indicator2 = "BMI is healthy weight"
             st.success(f"Well done {bmi_indicator2}. Your BMI is {bmi}")
         elif bmi >= 25 and bmi <= 30:
             bmi_indicator3 = "BMI is overweight"
             st.info(f"Oh no, {bmi_indicator3} Your BMI is {bmi}")
         elif bmi > 30:
             bmi_indicator4 = "BMI is obese"
             st.error(f"Oh no, {bmi_indicator4}. Your BMI is {bmi}")