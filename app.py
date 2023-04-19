import streamlit as st

def my_func(a, b, c, reset=0):
    lis = [a, b, c]
    lis.sort()
    if reset:
        st.write("")
        return
    out_str = "The largest number among the inputs is " + str(lis[-1])
    st.write(out_str)
st.set_page_config(page_title="22f2001467", layout="wide")

st.subheader("Streamlit App")
st.title("Largest Number")

first = st.number_input(label="Enter First Number")
second = st.number_input(label="Enter Second Number")
third = st.number_input(label="Enter Third Number")

largest = st.button("Find Largest")
if largest:
    my_func(first, second, third)
reset = st.button("Reset")
if reset:
    first = 0
    second = 0
    third = 0
    my_func(first, second, third, 1)

