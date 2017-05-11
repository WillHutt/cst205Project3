from pytesseract import image_to_string
from PIL import Image
from PIL import ImageEnhance


#greyscale    
img = Image.open('templates/pictures/user_upload.jpg').convert('L')      ##Use original image and convert to contrast
img.save('newSlide_1_grey.jpg')                  

#read to file
f = open("text.txt","w")
f.write(image_to_string(img))
f.write("\n")
f.close()