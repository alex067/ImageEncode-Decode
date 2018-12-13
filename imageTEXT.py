from PIL import Image
import binascii
def writeSize(image,textSize):
	binSize = 32-len(textSize)
	lastCol = image.size[0]-1
	lastRow = image.size[1]-1
	#NOTE: binsize will always be divisible by 8
	while binSize > 0: #fill in 0s till textSize
		r,g,b = image.getpixel((lastCol,lastRow))
		red = list(bin(r)[2:].zfill(8))
		green = list(bin(g)[2:].zfill(8))
		blue = list(bin(b)[2:].zfill(8))
		red[7] = '0'
		red = "".join(red)
		red = int(red,2)
		binSize -=1
		green[7] = '0'
		green = "".join(green)
		green = int(green,2)
		binSize -=1
		blue[7] = '0'
		blue = "".join(blue)
		blue = int(blue,2)
		binSize-=1
		tupBin = (red,green,blue)
		image.putpixel((lastCol,lastRow),tupBin)
		lastCol -=1
	#begin writing all bits of size
	binSize = len(textSize)-1
	writeBin = 0	
	while binSize >= 0: 
		r,g,b=image.getpixel((lastCol,lastRow))
		red = list(bin(r)[2:].zfill(8))
		green = list(bin(g)[2:].zfill(8))
		blue = list(bin(b)[2:].zfill(8))
		red[7] = textSize[writeBin]
		red = "".join(red)
		red = int(red,2)
		binSize -=1
		writeBin+=1
		green[7] = textSize[writeBin]
		green = "".join(green)
		green = int(green,2)
		binSize -=1
		writeBin+=1
		if binSize < 0:
			blue[7] = '0'
			blue = "".join(blue)
			blue = int(blue,2)
			tupBin = (red,green,blue)
			print (tupBin)
			image.putpixel((lastCol,lastRow),tupBin)
			break
		blue[7] = textSize[writeBin]
		blue = "".join(blue)
		blue = int(blue,2)
		binSize -=1
		writeBin +=1
		tupBin = (red,green,blue)
		print (tupBin)
		image.putpixel((lastCol,lastRow),tupBin)
		lastCol -=1
	print ("Size succesfully embedded!")
	
	
def writeText(image,text,size):
	print ("Embedding text message...")
	lastCol = image.size[0]-12
	lastRow = image.size[1]-1
	writeBin = 0 #for every 8 bits
	writePix = 0 #for each char
	numofPix = len(text) #length of message list
	pixel = text[writePix] #first character
	while size > 0:
		print (pixel)
		r,g,b = image.getpixel((lastCol,lastRow))
		red = list(bin(r)[2:].zfill(8))
		green = list(bin(g)[2:].zfill(8))
		blue = list(bin(b)[2:].zfill(8))
		red[7] = pixel[writeBin]
		red = "".join(red)
		red = int(red,2)
		writeBin +=1
		size -=1
		if writeBin == 8: #we read 8 bits
			writeBin = 0 #reset
			writePix += 1 #move to next pix
			if writePix == numofPix:
				break
			else:
				pixel = text[writePix]
		if size == 0: #finished reading
			green = "".join(green)
			green = int(green,2)
			tupBin = (red,green,blue)
			image.putpixel((lastCol,lastRow),tupBin)
			break
		green[7] = pixel[writeBin]
		green = "".join(green)
		green = int(green,2)
		writeBin +=1
		size -=1
		if writeBin == 8:
			writeBin = 0
			writePix += 1
			if writePix == numofPix:
				break
			else:
				pixel = text[writePix]
		if size == 0:
			blue = "".join(blue)
			blue = int(blue,2)
			tupBin = (red,green,blue)
			image.putpixel((lastCol,lastRow),tupBin)
			break
		blue[7] =pixel[writeBin]
		blue = "".join(blue)
		blue = int(blue,2)
		tupBin = (red,green,blue)
		image.putpixel((lastCol,lastRow),tupBin)
		writeBin+=1
		size-=1
		if writeBin == 8:
			writeBin = 0
			writePix += 1
			if writePix == numofPix:
				break
			else:
				pixel = text[writePix]
		if size == 0:
			break
		lastCol -= 1
	print("Text succesfully embedded!") 
print ("Please enter the path to the image:")
path = input('> ')
print ("Please enter the message to embbed:")
text = input('> ')
size = len(text)*8   #size to bits      
textSize = bin(size)[2:].zfill(8)
#binary conversion of string
binText = [bin(ord(ch))[2:].zfill(8) for ch in text]
img = Image.open(path).convert("RGB");
writeSize(img,textSize)
writeText(img,binText,size)
#save new image
print ("Save the image as...")
newImg = input('> ')
img.save(newImg,"PNG")
