# -*- coding: utf-8 -*-
"""Programa Codificador (Bit Menos Significativo).py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16yY3-w1LAMOOWRBjvloRW266zMdTnTEz
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:17:37 XXXX

@author: eduardo
"""
# Encoder for bmp images

# Importing libraries
from PIL import Image

# Converts a string to binary using ASCII encoding
def textToBinary(text):
    return ''.join((format(ord(i), 'b')).zfill(8) for i in text)

# Getting user input to find which file to open
print('Enter image file to open:')
imgIn = input()
print('Enter text to encode:')
textIn = input()
print('Enter image file to write to:')
imgOut = input()

# Taking our message, converting to binary
messageBin = textToBinary(textIn)

# Loading an image's pixel data
img_pre = Image.open(imgIn)
width, height = img_pre.size
pixels = img_pre.load()

# Changing the least significant bit of each pixel to match each bit of our encoded message
currBit = 0;
for x in range(0, width):
    if (currBit >= len(messageBin)):
        break

    # Getting the current pixel
    currPix = pixels[x, 0]
    #print('[%d, %d]: [%d, %d, %d]'%(x, 0, currPix[0], currPix[1], currPix[2]))

    # Changing the r, g, and b values of the pixel
    newPix = list(currPix)
    for c in range(0, 3):
        if (currBit >= len(messageBin)):
            break
        colorBin = list(format(currPix[c], 'b').zfill(8))
        colorBin[7] = messageBin[currBit]
        colorBin = ''.join(colorBin)
        newPix[c] = int(colorBin, 2)

        currBit += 1

    # Overwriting old pixel
    currPix = tuple(newPix)
    pixels[x, 0] = currPix

    # Displaying the modified pixel
    #print('  -> [%d, %d, %d]'%(currPix[0], currPix[1], currPix[2]))
    #print('  (%c, %c, %c)'%(messageBin[currBit-3], messageBin[currBit-2], messageBin[currBit-1]))

# Rewriting the image's pixel data to a new image
img_pre.save(imgOut)