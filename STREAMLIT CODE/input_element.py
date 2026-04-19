import streamlit as stl

stl.title("Different types of Input",anchor=False)
stl.divider()

name = stl.text_input("Enter your name",placeholder="Type your name here")
stl.write("Your name is: ",name)

stl.divider()
age = stl.number_input("Enter your age",value=None,placeholder="Type your age here")
#print(type(age))
stl.write("Your age is: ",age)
stl.divider()

pressed = stl.button("Submit",type="primary")
if pressed:
    stl.write(f"Your name is {name} and your age is {age}")

password = stl.text_input("Enter your password",type="password",placeholder="Type your password here")
print(type(password))
stl.write("Your password is: ",password)

selected = stl.selectbox("choose your profession",["Student","Teacher","Developer","Doctor","Other"],
                         index=None,placeholder="choose or add option",accept_new_options=True)
#print(type(selected))
stl.write("Your profession is: ",selected)
stl.divider()