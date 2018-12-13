from PIL import Image
from collections import deque
import binascii
def extractMsg(text): #function which converts the binary to int value
	ext = int(text,2)
	return ext

def decodeSize(image): #extracting the size
	counter = 32 #number of bits
	size = "" #constructing binary string
	lastCol = image.size[0]-1
	lastRow = image.size[1]-1
	while (counter >  0):
		r,g,b = image.getpixel((lastCol,lastRow))
		red = list(bin(r)[2:].zfill(8))
		green = list(bin(g)[2:].zfill(8))
		blue = list(bin(b)[2:].zfill(8))
		rred = red[7]
		ggreen = green[7]
		bblue = blue[7]
		size += rred #construct string from bits
		counter -= 1
		size += ggreen 
		counter -= 1
		if counter == 0:#if we hit 32
			return extractMsg(size)
		size += bblue 
		counter -= 1
		lastCol = lastCol -1

def decodeMsg(image,size):
	lastCol = image.size[0]-12
	lastRow = image.size[1]-1
	msg = "" #string containing 8 bits
	totalmsg = [] #list of binaries 
	bitscount = 0 #every 8 we append
	while size > 0: 
		r,g,b = image.getpixel((lastCol,lastRow))
		red = list(bin(r)[2:].zfill(8))
		green = list(bin(g)[2:].zfill(8))
		blue = list(bin(b)[2:].zfill(8))
		bblue = blue[7]
		rred = red[7]
		ggreen = green[7]
		msg += rred
		size -= 1
		bitscount += 1
		if bitscount == 8: #every 8 bits read
			ext = extractMsg(msg)
			totalmsg.append(ext) #add binary to list
			msg = "" #reset
			bitscount = 0 #reset
		if size ==  0: #manually break 
			break
		msg += ggreen
		size -= 1
		bitscount += 1
		if bitscount == 8:
			ext = extractMsg(msg)
			totalmsg.append(ext)
			msg = "" #reset for new byte retrieval
			bitscount = 0 #reset 	
		if size == 0:
			break
		msg += bblue
		size -= 1
		bitscount += 1
		if bitscount == 8:
			ext = extractMsg(msg)
			totalmsg.append(ext)
			msg = ""
			bitscount = 0;
		if size == 0:
			break
		lastCol = lastCol -1
	#begin constructing the values
	hiddenmsg = []
	for pixel in totalmsg: #convert each int value to ascii
		val = chr(pixel)
		hiddenmsg.append(val)
	return "".join(hiddenmsg)

print ("Please enter the image to decode:")
path = input('> ')
img = Image.open(path).convert("RGB")
textSize = decodeSize(img)
print ("The size of the hidden message is: ",textSize)
print ("The hidden message contained in the message is... ")
print (decodeMsg(img,textSize))

