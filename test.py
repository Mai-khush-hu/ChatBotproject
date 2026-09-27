import streamlit as st
import math

st.title(" 🧮 Calculator Program")

a = st.number_input("Enter a Number",value=0.0)
b = st.number_input("Enter another Number",value=0.0)

operation = st.selectbox("Choose Operations",["Add","Subtract","Multiply","Divide","Modulus","Floor Division","Power","Square root","Log Values base 10"])

if st.button("Calculate"):
    if operation == "Add":
        result=a+b
    elif operation == "Subtract":
        result=a-b
    elif operation == "Multiply":
        result=a*b
    elif operation == "Modulus":
        result=a%b
    elif operation == "Floor Division":
        result=a//b
    elif operation == "Power":
        result=a**b
    elif operation == "Square root":
        result=math.sqrt(a)
    elif operation == "Log Values base 10":
        result=math.log10(a)
    else :
        result=a/b


    st.write("Result:", result)





with st.sidebar:
    st.write("This is sidebar")
    st.button("Sidebar button")
    st.button("New Chats")
    