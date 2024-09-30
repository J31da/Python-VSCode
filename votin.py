import streamlit as st

st.header(':blue[**Who Do You Think Will Win**]')
st.divider()

trumpv = 0
kamalav = 0

vtt1,vtt2 = st.columns([0.5,0.3])

with vtt1:
    age = st.number_input('How Old Are You? ',value=0)

    if age >= 18:
        vote = st.text_input("Who do you want to vote for? (Donald Trump/Kamala Harris): ")
        if vote == 'Donald Trump':
            trumpv += 1
            st.success('Vote Recorded for Trump')
        elif vote == 'Kamala Harris':
            kamalav += 1
            st.success('Vote Recorded for Kamala')

    else:
        st.warning('Not Old Enough To Vote')

st.write('')
vt1,vt2 = st.columns(2)
with vt1:
    st.subheader('Donald Trump')
    print(trumpv)
with vt2:
    st.subheader('Kamala Harris')
    print(kamalav)
