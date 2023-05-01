import os
import cv2 as cv 

# Read image to get best resolution and get the dimension of the wihte background 
img1 = cv.imread('background.png', cv.IMREAD_UNCHANGED)
# get resolution , the dimension of the photo 
height, width, channels = img1.shape
print(f'{height},  {width}, {channels}')

counter =1 
#ROOT ,  DIRCTORY , FILE 
for r, d, f in os.walk(".\\kk\\"): 
    print(f)
    for file in f:
        try:
            print(file)

            print(counter)
            img2 = cv.imread('.\\kk\\' + file, cv.IMREAD_UNCHANGED)
            print('oregnal Dimensions : ',img2.shape)
        
            # resize the image , i'm going to apply a kind of reducing to it in order to get the fit of my photo , downscaling 
            img3 = cv.resize(img2, (width, height) , interpolation=cv.INTER_AREA)
            print('Resized Dimensions : ',img3.shape)
            # save new image on test2 folder
     
            cv.imwrite(".//LL//"+file, img3)

            counter= counter +1

        
        except Exception as e:
            print(str(e))




