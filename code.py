import cv2 as cv
from PIL import Image
import numpy as np
import glob
import os
cv_img = []
#width and height of temprory image
width1, height1 = 1280,720
name2='black_Merged'
#Merging images 
def merging(image1,image2):
    result = cv.addWeighted(image1, 1,image2, 1, 0.0)
    return result
#Creating a blank numpy iamge
def create_blank(width, height):
    image = np.zeros((height, width, 3), np.uint8)
    return image
#Getting the path
path = glob.glob("LL Broadcast 1 - 10 Segmentation/*")

#loop till all director
for i in range(len(path)):
    #Getting all image Directories 
    labellist=glob.glob(path[i]+"/*.png")
    image = create_blank(width1, height1)
    name=os.path.basename(path[i])
    #Getting all images present in the directories
    for j in range(len(labellist)):
        image2=cv.imread(labellist[j])
        if image2 is not None:
            result=merging(image,image2)
            image=result
    #Saving merged Images with black background
    cv.imwrite('Merged/Black/'+name+".png", result)
    img = Image.open('Merged/Black/'+name+".png")
    #Conerting the background to a transparent 
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    #Saving Image with transparent background
    img.putdata(newData)
    img.save('Merged/Transparent/'+name, "PNG")
