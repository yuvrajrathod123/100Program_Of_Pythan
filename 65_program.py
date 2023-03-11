
# program to find the resolutions(size) of a image using poillow module 

import PIL
from PIL import Image

img = PIL.Image.open("C:/Users/Mtronics Computers/Downloads/face-recognition.png")
width,height = img.size

print(width ,"x",height)
