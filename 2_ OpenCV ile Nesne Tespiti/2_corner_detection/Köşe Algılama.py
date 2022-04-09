import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)#resin float turune cevrilir
print(img.shape)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

# harris corner detection  #blocksize=pixellerin komşulugu ,ksize=kutucuk boyutu,k=harris detectordeki free paramtere
dst = cv2.cornerHarris(img, blockSize = 2, ksize = 3, k = 0.04)
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off")

dst = cv2.dilate(dst, None)#genişletme yapılır
img[dst>0.2*dst.max()] = 1#noktalamalar resmin max degerinin %20 sinden buyukse degerlere 1 ata beyaz olsun noktalar
plt.figure(), plt.imshow(dst, cmap = "gray"), plt.axis("off")


# shi tomasi detection
img = cv2.imread("sudoku.jpg", 0)
img = np.float32(img)
corners = cv2.goodFeaturesToTrack(img, 120, 0.01, 10)#120 sayısı koşe sayısı,0,01 kalite,minimum distane iki koşe arası
corners = np.int64(corners)#integera çevrilir

for i in corners:
    x,y = i.ravel()#ravel düzleştirme
    cv2.circle(img, (x,y),3,(125,125,125),cv2.FILLED)
    #daire oluştur (resmei(x ve y noktası),yarıçap,(renk),dairenin içi doldurulur)
plt.imshow(img)
plt.axis("off")