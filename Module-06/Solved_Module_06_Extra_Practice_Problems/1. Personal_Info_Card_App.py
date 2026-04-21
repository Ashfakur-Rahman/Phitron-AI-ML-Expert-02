import streamlit as st
st.title("Personal Info Card App",anchor=False)

name = st.text_input("Enter your name",placeholder="Ashfakur Rahman")
age = st.number_input("Enter your age")
profession = st.selectbox(
    "Choose your occupation: ",
    ["Student","Employee","Businessman","Freelancer"]
)
submit = st.button("Submit")
if submit:
    st.text(f"Name is: {name}\nAge is: {age}\nOccupation: {profession}")
else:
    st.markdown(":red[Please fill out the form and click submit to see your personal info card.]")