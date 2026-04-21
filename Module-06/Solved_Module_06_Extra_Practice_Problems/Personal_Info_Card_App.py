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
    if not name or not age or not profession:
        st.warning("⚠Please fill in all the fields before submitting.")
    else:
        st.success("Your information has been submitted successfully!")
        st.text(f"Name is: {name}\nAge is: {age}\nOccupation: {profession}")