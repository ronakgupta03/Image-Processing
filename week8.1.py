# from PIL import Image


# #opening the image
# img = Image.open('image1.png')


# #Image in genearl compuers process them in terms of matrics so that image is opened 
# # the corresponding matrix format is taken and capture by this object img the matrix
# # fomrat is capture here and flipping theiamge is the terminlogy that we are using
# # here to actually convert the mirror image into actual image we are using the terminalogy
# # for the thing that is easy on our mind buy thte techinical temrinallogy that they users 
# # transposing - making rows as coloums and colums as rows

# #transposing
# transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# #Save it to a file in a human understandble format

# transposed_img.save('image1output.png')

# print("Done Flipping")

from PIL import Image

# Open the image using the full path
img = Image.open("/image1.png")

# Flip the image horizontally
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

# Save the flipped image
transposed_img.save("/image1output.png")

print("Done Flipping")



