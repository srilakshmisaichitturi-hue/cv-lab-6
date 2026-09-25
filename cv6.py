import cv2
import numpy as np
from matplotlib import pyplot as plt
#Load the image in grayscale
img=cv2.imread("nature.jpg",0)
if img is None:
  print("Error: Image not found")
else:
  #set up the plot figure
  plt.figure(figsize=(12,10))
  #display original image
  plt.subplot(3,3,1)
  plt.imshow(img,cmap='gray')
  plt.title("original image")
  plt.axis("off")
  #loop through all 8 bit planes
  for i in range(8):
    #Extract the i-th bit plane
    #shift bits right by i and perform bitwise AND with 1
    bit_plane=(img>>i)&1

    #scale to 0-255 for visualization (0 becomes black,1 becomes white)
    vis_plane=bit_plane*255
#plotting
    plt.subplot(3,3,i+2)#position starts from 2
    plt.imshow(vis_plane,cmap='gray')
    plt.title(f"bit plane {i}")
    plt.axis("off")

plt.tight_layout()
plt.show()
