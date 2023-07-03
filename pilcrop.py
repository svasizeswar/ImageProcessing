#Import required Image library
from PIL import Image

#Create an Image Object from an Image
im = Image.open('images/search.png')

 

#left, upper, right, lowe
#Crop
cropped = im.crop((0,0,300,300))
 

#Save the cropped image
cropped.save('images/croppedBeach1.png')