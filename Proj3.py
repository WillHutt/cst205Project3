from pytesseract import image_to_string
from PIL import Image
from PIL import ImageEnhance

#Image resizing based on percentage         `##Check to see which filters work best
basewidth = 500
image = Image.open('user_image.jpg')         ##Use original image                 
width_percent = (basewidth/float(image.size[0]))
height_size = int((float(image.size[1])*float(width_percent)))
image = image.resize((basewidth,height_size), Image.ANTIALIAS)
image.save('newSlide_1.jpg')                 ##Resized image

#greyscale                                  ##Check to see which filters work best
img1 = Image.open('user_image.jpg').convert('L')      ##Use original image
img1.save('newSlide_1_grey.jpg')                  ##Only greyscale
img2 = Image.open('newSlide_1.jpg').convert('L')      ##Use resized image
img2.save('newSlide_1_re_grey.jpg')               ##Greyscale and resize

#contrast                                   ##Check to see which filters work best
contr = ImageEnhance.Contrast('user_image.jpg')       ##Use original image
im = contr.enhance(1.8)
im.save('newslide_1_contr.jpg')               ##Only contrast
contr2 = ImageEnhance.Contrast('newSlide_1.jpg')         ##Use resized image
im2 = contr2.enhance(1.8)
im2.save('newSlide_1_re_contr.jpg')           ##Resize and contrast
contr3 = ImageEnhance.Contrast('newSlide_1_grey.jpg')    ##Use greyscale image
im3 = contr3.enhance(1.8)
im3.save('newSlide_1_grey_contr.jpg')         ##Greyscale and contrast
contr4 = ImageEnhance.Contrast('newSlide_1_re_grey.jpg') ##Use resized greyscale image
im4 = contr4.enhance(1.8)
im4.save('newSlide_1_re_grey_contr.jpg')      ##Resize, greyscale, contrast

#read to file
f = open("text.txt","w")
f.write(image_to_string(image))
f.write(" ")
f.write(image_to_string(img1))
f.close()