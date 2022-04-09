import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("contour.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

# farklı sürüm için 
# image, contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

                 #contour bul(resimden,iç ve dış kontourleri alır,yatay dikey ve çarpraz bolumle sıkıştırır sadece uç noktaları kalır)
contours, hierarch = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# hierarch=iç ve dıştan alınan kontourleri belirtir
external_contour = np.zeros(img.shape)
internal_contour = np.zeros(img.shape)

for i in range(len(contours)):#kontourların uzaklıkları
    
    # external
    if hierarch[0][i][3] == -1:#0.indexinin i ninci indexinin 3.indexi -1 e eşitse bu dış kontourdur
        cv2.drawContours(external_contour,contours, i, 255, -1)
    #contour çiz(çizilcek kontor turu,conourleri çizelim,i ninci index,renk,kalınlık -1 ise kontourlar ile sınırlanan alanı doldur anlamına gelir)
    else: # internal
        cv2.drawContours(internal_contour,contours, i, 255, -1)

plt.figure(), plt.imshow(external_contour, cmap = "gray"),plt.axis("off")#dış kontour
plt.figure(), plt.imshow(internal_contour, cmap = "gray"),plt.axis("off")#iç kontour
