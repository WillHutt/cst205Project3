https://github.com/IceCube1333/cst205Project3

Picture to Text

William Hutt
Matt Guyadeen
Gildardo 

CST205
5/16/17

Program is run through app.py


 languages/libraries used:

PIL, tesseract, Flask, HTML, CSS, and Python

How it works:

In order to upload you image simply click on the choose file button. 
Then choose the photo you want to upload and click on the upload button. 
To download the text that was converted from the photo simply click on the 
download button.


Thoughts:

We considered adding in an email portion but decided against it due to the lack of time remaining.


Who did what:

Will: 
Was in charge of making the website, uploading to the website, and downloading from the website.
When uploading the picture it's name is turned into user_upload.jpg which made it easy to hardcode into 
the text_pickup.py that we made for project 2. Downloading simply downloads the text.txt file that
is made from uploading the photo and extracting the text from it. Also linked the text_pickup.py to the
app.py so that when app.py is run so is text_pickup.py and also removed unnecessary filters.

Matt:
Was in charge of updating the text_pickup.py so that the uploaded photos would run through the filters.
Put into the filters the uploaded file called user_upload.jpg.

Gildardo:
Was in charge of working on email. Needed to update the code from project 2 to work with project 3 or
come up with something new to work on the website. This was not done so the idea was scrapped due to
lack of time/poor time management.