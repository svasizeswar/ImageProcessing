import cv2
import numpy as np 
import glob
import os
def leftToRight(img,imageWidth,imageHeight):

    # [rows, columns]    
    inc_list = list(np.arange(width_partion_inc,imageWidth,width_partion_inc))
    par_list = list(np.arange(width_partion_par,imageWidth,width_partion_par)) 
    star_width = 0
    for width in par_list:  
        par_crop = img[0:imageHeight, star_width:width]  
        cv2.imwrite('images/cropped/'+image_name+'-lr-par-'+str(width)+'.png',par_crop) 
        star_width = width

    for width in inc_list:         
        inc_crop = img[0:imageHeight, 0:width]  
        cv2.imwrite('images/cropped/'+image_name+'-lr-inc-'+str(width)+'.png',inc_crop)    

def rightToLeft(img,imageWidth,imageHeight):

    # [rows, columns]    
    inc_list = list(np.arange(width_partion_inc,imageWidth,width_partion_inc))
    for width in inc_list:  
        if not imageWidth-width < width_partion_inc:
            inc_crop = img[0:imageHeight, width:imageWidth]  
            cv2.imwrite('images/cropped/'+image_name+'-rl-inc-'+str(width)+'.png',inc_crop)  

def bottomToTop(img,imageWidth,imageHeight):

    # [rows, columns]    
    inc_list = list(np.arange(height_partion_inc,imageHeight,height_partion_inc))
    #print("List", inc_list)
    for height in inc_list:
        if not imageHeight-height < height_partion_inc: 
            inc_crop = img[height:imageHeight, 0:imageWidth]  
            cv2.imwrite('images/cropped/'+image_name+'-bt-inc-'+str(height)+'.png',inc_crop)                    

def topToBottom(img,imageWidth,imageHeight):
    
    list_par = list(np.arange(height_partion_par,imageHeight,height_partion_par))
    list_inc= list(np.arange(height_partion_inc,imageHeight,height_partion_inc))
    #print("List", inc_list)    
    star_height = 0
    for height in list_par:  
        par_crop = img[star_height:height, 0:imageWidth]  
        cv2.imwrite('images/cropped/'+image_name+'-tb-par-'+str(height)+'.png',par_crop)  
        star_height = height

    for height in list_inc:        
        inc_crop = img[0:height, 0:imageWidth]  
        cv2.imwrite('images/cropped/'+image_name+'-tb-inc-'+str(height)+'.png',inc_crop) 

def spliceImg(img,imageWidth,imageHeight):
    for i in range(0,nRows):
        for j in range(0, mCols):
            roi = img[int(i*imageHeight/nRows):int(i*imageHeight/nRows + imageHeight/nRows) ,int(j*imageWidth/mCols):int(j*imageWidth/mCols + imageWidth/mCols)]
            cv2.imwrite('images/cropped/'+image_name+'-sp-'+str(i)+str(j)+".png", roi)


path = "images/*.png"
for file in glob.glob(path):
    print(file) 

    img = cv2.imread(file)
    print(type(img))

    image_name  = os.path.basename(file)
    
    # Shape of the image
    image_copy = img.copy() 
    imageHeight = img.shape[0]
    imageWidth = img.shape[1]
    #print("Height of the image", imageHeight)
    #print("Width of the image", imageWidth)

    width_partion_inc = int(imageWidth/10)
    height_partion_inc = int(imageHeight/10)
    width_partion_par = int(imageWidth/10)
    height_partion_par = int(imageHeight/5)
    nRows = 2
    mCols = 4

    spliceImg(img,imageWidth,imageHeight) 
    leftToRight(img,imageWidth,imageHeight)
    rightToLeft(img,imageWidth,imageHeight)
    bottomToTop(img,imageWidth,imageHeight)
    topToBottom(img,imageWidth,imageHeight)

        
