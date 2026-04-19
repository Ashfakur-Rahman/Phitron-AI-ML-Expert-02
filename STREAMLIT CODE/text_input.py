import streamlit as stl
#stl.write("This is a text input example")
stl.title("My first streamlit web app",anchor=False)
stl.header("This is a header",divider=True)
stl.subheader("This is a sub header")
stl.text("This is a text")

stl.markdown(":red[**RED BOLD**] *Italic* :orange[Orange markdown]")
stl.markdown(":red-background[:red[**RED BOLD**] *Italic* :orange[Orange markdown]]:world_map:")

a = 20
b = 30
c = 40
stl.write("The value of a, b, c is ",a,b,c)