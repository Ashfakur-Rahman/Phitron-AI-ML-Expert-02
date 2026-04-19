import streamlit as stl
stl.title("Input your (video) files",anchor=False)
stl.divider()

#from directory
stl.video("Video/videography.mp4")

#from url
stl.video("https://www.youtube.com/watch?v=JnvWYDDxFuA")

video = stl.file_uploader("Select your video file",
                          type=["mp4","avi", "mkv"],accept_multiple_files=False)
button = stl.button("Confirm to upload")
if button:
    if video:
        stl.video(video)
        stl.success("Your video file has been uploaded successfully!")
    else:
        stl.error("No video file selected. Please choose a file to upload.")
else:
    stl.error("No video file selected. Please choose a file to upload.")
