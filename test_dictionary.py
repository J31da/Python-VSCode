#1 Create A Dictionary with 5 Attributes & display it on streamlit

#2 Convert this dictionary to A Dataframe & display it on streamlit

#1

import streamlit as st
import pandas as pd

info_dict = {
    "First Name" : ["Jeida"],
    "Last Name" : ["Adewusi"],
    "Age" : [13],
    "Date Of Birth" : ["2010"],
    "Nationality" : "Nigerian",
}

st.write(info_dict)

#2

info_df = pd.DataFrame(info_dict)
st.dataframe(info_df,use_container_width=True)