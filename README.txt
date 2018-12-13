ALEXANDROS PANAYI
!!Embedding messages to pictures!!

Contents:
1. About
2. Installation
3. How-to
4. Known bugs & errors
---------------------------------------------------------------
ABOUT
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The purpose of this program is to embedd string messages within pictures.
It is done so by extracting the RGB values of the picture, and modifying
the least significant bits of the pixels found on the bottom right, to 
hide the size of the message, along with the message itself.

imageTEXT.py :: identify a picture to store a hidden message
readIMAGE.py :: identify a picture to reveal hidden message

INSTALLATION
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Use the following commands in the terminal in order:
-python3 imageTEXT.py
-python3 readIMAGE.py

Picture must be in jpg extension, outputs as png extension.

HOW-TO
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Running the imageTEXT.py script, you will have to enter the direct 
path directory where the image is located. For example: "\home\user\
Desktop\testpicture.jpg"

After providing the image location, enter the desired message to embedd 
in the current picture. 

Shortly after, please provide the new name you would like on your newly
formatted message, containing your new secret hidden message! spooky!

Your new picture will be located in: "\home\user\Desktop\"

Run the readIMAGE.py script, where you will be prompted to specifiy the location
of the new image, which was obtained from before. 

Be prepared to be amazed!


