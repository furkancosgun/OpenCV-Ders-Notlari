import cv2
import matplotlib.pyplot as plt

# resmi içe aktar
img = cv2.imread("img1.jpg")

#resmi goster
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#convertcolor(resim.cv2.bgr deger)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()


# eşikleme
#iki değer return eder resmimize=cv2...(resmimiz,thresh=degeri uzerindeki yerler beyaz olur,maxval=resim degerleri 0 ile 255 arasında
#,type=thersh.binary ve thersh.binary.inv turleri vardır)
#thershbinary:thersh degeri  ve max deger arasını siler
#thershbinar.inv:thersh degeri ve max deger arasında olömayan kısmı siler
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY)

plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

# uyarlamalı eşik değeri  (resim,maxvalue,tresh hold degerini alır,tresh hold tipi,blok size pixel toplulugu,tresh hold degeri)
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,8)
plt.figure()
plt.imshow(thresh_img2, cmap = "gray")
plt.axis("off")
plt.show()

























