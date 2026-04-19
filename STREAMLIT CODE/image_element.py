import streamlit as stl
stl.title("Input your (image) files",anchor=False)
stl.divider()

#from directory
stl.image("image/img1.jpeg")

#from url
stl.image("https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60")


stl.divider()

image =stl.file_uploader("Select your image",
                  type=["jpg","jpeg","png"],accept_multiple_files=True)
print(type(image))

# if image:
#     for img in image:
#         stl.image(img)  # showing all images in one column

if image:
    if len(image) > 3:
        stl.warning("You can only upload a maximum of 3 images. Please select up to 3 images.")
    else:
        col = stl.columns(len(image))  # showing all images in different columns
        for i, img in enumerate(image):
            col[i].image(img)