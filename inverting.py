import cv2
import numpy as np
from PIL import Image


img = cv2.imread('foto.png', 0)
cv2.imshow("foto",img)
cv2.waitKey()

def invert (img):
    
    
    max = img[0][0]
    for i in range(m):
        for j in range(n):
            if (img[i][j]>max):
                max = img[i][j]
                
    for i in range(m):
        for j in range(n):
            img[i][j] = max - img[i][j]
            
    
    inverted_img = Image.fromarray(img)
 
    # tersini aldığım görüntüyü kaydetme 
    inverted_img.save(r"inverted.jpg") 
    img2 = cv2.imread('inverted.jpg')
    cv2.imshow("foto2",img2)
    cv2.waitKey()
     
            
m, n = img.shape  
invert(img)



#kendi metodumu test etme

img3 = cv2.imread('foto.png', 0)
img3 = np.invert(img3)
#img3 = cv2.imread('foto.png', 0)
cv2.imshow("fotonp",img3)
cv2.waitKey()