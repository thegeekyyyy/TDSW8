import streamlit as st     

#function to find the largest number among a, b, c
def largest_number(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    

#stramlit ui
st.title("Find the largest among the three given numbers")
a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
c = st.number_input("Enter the third number")
if st.button("Find Largest"):
    result = largest_number(a,b,c)
    st.success(f"The largest number is {result}")
