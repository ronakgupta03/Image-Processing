#Image enhancement
#adaptive histrogram equalisation technique or enhancement technique we call it as clahe 


import cv2 

#read the image
img = cv2.imread("/image2.jpeg")  #find ~/ -name "image2.png"

#Preperation of CLAHE
clahe = cv2.createCLAHE()

#Convert to gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply enhancement
enh_img = clahe.apply(gray_img)


#save it a file
cv2.imwrite("/image2out.jpeg", enh_img)

print("Done enhancing")



