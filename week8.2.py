#Image enhancement
#adaptive histrogram equalisation technique or enhancement technique we call it as clahe 


import cv2 

#read the image
img = cv2.imread("/home/asus-ronak/Desktop/Joy of Python/image processing/finger.jpg")  #find ~/ -name "image2.png"

#Preperation of CLAHE
clahe = cv2.createCLAHE()

#Convert to gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#apply enhancement
enh_img = clahe.apply(gray_img)


#save it a file
cv2.imwrite("/home/asus-ronak/Desktop/Joy of Python/image processing/fingerout.jpeg", enh_img)

print("Done enhancing")



