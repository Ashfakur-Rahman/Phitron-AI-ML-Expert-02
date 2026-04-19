import streamlit as stl
stl.title("Input your (audio) files",anchor=False)
stl.divider()

#from directory
stl.audio("Audio/hum kis gali.mp3",loop=True) # loop=True means the audio will play repeatedly until the user stops it.

#form url
stl.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",loop=True)


audio = stl.file_uploader("Select your audio file",
                          type=["mp3","wav", "flac"],accept_multiple_files=False)
if audio:
    stl.audio(audio)