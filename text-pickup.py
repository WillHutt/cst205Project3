#from pytesseract import image_to_string
import pytesseract
from PIL import Image
from PIL import ImageEnhance
import shutil

import smtplib
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

#Image resizing based on percentage
# basewidth = 500
# image = Image.open('static/pictures/user_upload.jpg')
# width_percent = (basewidth/float(image.size[0]))
# height_size = int((float(image.size[1])*float(width_percent)))
# image = image.resize((basewidth,height_size), Image.ANTIALIAS)
# image.save('static/pictures/user_upload.jpg')

#greyscale
img1 = Image.open('static/pictures/user_upload.jpg').convert('L')
img1.save('static/pictures/user_upload.jpg')

#pictures
on = Image.open("static/pictures/user_upload.jpg")


#contrast
#const = ImageEnhance.Contrast(on)
#im = const.enhance(1.8)
#im.save('static/pictures/user_upload.jpg')

#pictures after contrast
new4low = Image.open("static/pictures/new4slide5.jpg")
new2yo = Image.open("static/pictures/new2slide1.jpg")


#read to file
f = open("text.txt","w")
f.write(pytesseract.image_to_string(on))
f.write(" ")
f.write(pytesseract.image_to_string(on))
f.close()

shutil.move("text.txt", "static/text.txt")


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
attachment = open("static/text.txt", "rb")
 
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

