
from PIL import Image
import cv2
import numpy as np
import os, sys

def similar(a,b):
    w1 = a.width
    h1 = a.height
    w2 = b.width
    h2 = b.height
    goodpixels=0
    wrongpixels=0
    for x in range (1, w1, 1):
        for y in range (1, h1, 1):
            coordinate = x, y
            kolor1 = str(a.getpixel(coordinate))
            kolor2 = str(b.getpixel(coordinate))            
            #print("x: ",x,"y: ",y,"a.g",str(a.getpixel(coordinate)),"b.g",str(b.getpixel(coordinate)))
            if str(a.getpixel(coordinate))==str(b.getpixel(coordinate)):
                goodpixels = goodpixels + 1
            else: 
                wrongpixels = wrongpixels + 1
    """
    print("Good:", goodpixels)
    print("Wrong", wrongpixels)
    print((goodpixels/(w1*h1))*100,"%")
    """
    if goodpixels/(goodpixels+wrongpixels)>0.9:
        return True
    return False


#image1 = Image.open("ALAN_H1_DSC2575.JPG")
image1 = Image.open("file.JPG")
w1 = image1.width
h1 = image1.height
#image2 = Image.open("ALAN_H1_DSC2575v2.JPG")
image2 = Image.open("file.JPG")
w2 = image2.width
h2 = image2.height
if w1==w1&h1==h2:
    similar(image1,image2)
else:
    #print(w1,h1,w2,h2)
    """first same size : 700 / 700"""
    image1 = image1.resize((700, 700), Image.ANTIALIAS)
    image2 = image2.resize((700, 700), Image.ANTIALIAS)
    if similar(image1,image2):
        print("1Yes")
    else:
        print("1No")

    """print(image1.width,image1.height,image2.width,image2.height)"""

    """second same size : w2 / h2"""
    image1 = image1.resize((w2, h2), Image.ANTIALIAS)
    
    image2 = image2.resize((w2, h2), Image.ANTIALIAS)
    if similar(image1,image2):
        print("2Yes")
    else:
        print("2No")
    #print(image1.width,image1.height,image2.width,image2.height)
    """third same size : w1 / h1"""
    image1 = image1.resize((w1, h1), Image.ANTIALIAS)
    image2 = image2.resize((w1, h1), Image.ANTIALIAS)
    if similar(image1,image2):
        print("3Yes")
    else:
        print("3No")
    #print(image1.width,image1.height,image2.width,image2.height)