#from pytesseract import image_to_string
import pytesseract
from PIL import Image
from PIL import ImageEnhance

import smtplib
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

#Image resizing based on percentage
basewidth = 500
image = Image.open('pictures/slide5.jpg')
width_percent = (basewidth/float(image.size[0]))
height_size = int((float(image.size[1])*float(width_percent)))
image = image.resize((basewidth,height_size), Image.ANTIALIAS)
image.save('pictures/new2slide5.jpg')

#greyscale
img1 = Image.open('pictures/slide1.jpg').convert('L')
img1.save('pictures/newslide1.jpg')

#pictures
on = Image.open("pictures/powerpoint-presentation-ma-thesis-defence-6-728.jpg")
yo = Image.open("pictures/slide1.jpg")
newyo = Image.open("pictures/newslide1.jpg")
# low = Image.open("slide5.jpg")
# newlow = Image.open("newslide5.jpg")
# new2low = Image.open("new2slide5.jpg")
# new3low = Image.open("new3slide5.jpg")


#contrast
const = ImageEnhance.Contrast(newyo)
im = const.enhance(1.8)
im.save('pictures/new2slide1.jpg')

#pictures after contrast
new4low = Image.open("pictures/new4slide5.jpg")
new2yo = Image.open("pictures/new2slide1.jpg")

#tests for printing to see accuracy
# print(image_to_string(newyo))
# print " "
# print(image_to_string(new2yo))
# print " "
# print(image_to_string(on))

#read to file
f = open("text.txt","w")
f.write(pytesseract.image_to_string(on))
f.write(" ")
f.write(pytesseract.image_to_string(new2yo))
f.close()


#email
fromaddr = "whutt@csumb.edu"
toaddr = "whutt@csumb.edu"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Text from picture"
 
body = "Here is your text."
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "text.txt"
attachment = open("text.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print ("Sending mail to "+ toaddr)
mypwd = getpass.getpass('Enter your password: ') 
server.login(fromaddr, mypwd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print "Message sent"
server.quit()

