import cv2
import numpy as np      

def histogram(img):
      
    # her yoğunluk değerinin sayısını saklamak için oluşturulan boş liste
    count =[]
      
    # yoğunluk değerini saklamak için oluşturulan boş liste
    value = []
      

    for k in range(0, 256):
        value.append(k)
        count1 = 0
 
        for i in range(m):
            for j in range(n):
                if img[i, j]== k:
                    count1+= 1
        count.append(count1)
          
    return (value, count)
  
  
img = cv2.imread('foto.png', 0)
print (img)
cv2.imshow("zambak",img)
cv2.waitKey()
  

m, n = img.shape
print(histogram(img))   #burada return edilen diziler incelenebilir


#burada ise matplotlib kütüphanesini import ederek 
#histogram metodunun return ettiği değerler ile grafik çizdirdim
#ardından cv2 kütüphanesinin calcHist metodu ile görüntünün histogramını çizdirip 
#kendi yazdığım metodu kontrol ettim

import matplotlib.pyplot as plt
r, count = histogram(img)
plt.stem(r, count)
plt.xlabel('yoğunluk değeri')
plt.ylabel('piksel sayısı')
plt.title('görüntünün histogramı')

hist_gray_yeni = cv2.calcHist([img], [0],None,[256],[0,256])
plt.figure(1)
plt.stem(hist_gray_yeni)
