import streamlit as st

#sessionstate in streamlit keeps track of your variables everywhere for a particular user's session
# a callback function is used to code python to start a function before reading other code

# number = 5
# st.write(number)
# if st.button('Add 1'):
#     number +=1

# st.write(number)



if 'number' not in st.session_state:
    st.session_state.number = 0


number = st.number_input("Enter a number",key='number',value=0)
st.write(st.session_state.number)

def add():
    st.session_state.number +=1
if st.button('Add 1',on_click=add):
  pass


def remove():
 st.session_state.number -=1
if st.button('Remove 1',on_click=remove):
    pass

