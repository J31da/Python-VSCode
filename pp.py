import streamlit as st

#1.

no1,no2 = st.columns([0.3,0.4])
no3,no4 = st.columns([0.3,0.4])
no5,no6,no7 = st.columns([0.3,0.3,0.3])

with no1:
    num = st.number_input('Enter A Number: ')
    if num % 2 == 0:
        st.write('The number is even.')
    else:
        st.write('The number is odd.')


#2.

with no2:
    fruits = ['apple', 'banana', 'cherry', 'date', 'orange']
    st.write(fruits[2])


#3. 

with no3:
    people = {'John' : 10, 'Jenny' : 15, 'Jane' : 60}
    st.write(people['Jane'])


#4.

with no4:
    width = st.number_input('Enter the width of the rectangle: ')
    height = st.number_input('Enter the height of the rectangle: ')
    area = width * height
    st.write('The area of the rectangle is: ',area)


#5. 

with no5:
    string = st.text_input('Enter a string: ')
    st.write(string[::-1])


#6. 

with no6:
    for i in range(1,11):
      print(1)


#7.

with no7:
    numb = [1, 2, 3, 4, 5, 6]
    even_num = [num for num in numb if num % 2 == 0]
    st.write(even_num)