import cv2
import numpy as np

# içe aktar resim
img = cv2.imread("kart.png")
cv2.imshow("Orijinal", img)

width = 400
height = 500
                    #sol ust/sol alt/sag ust/sag alt
pts1 = np.float32([[200,1],[1,472],[540,150],[338,617]])#ilk resim koşe noktaları
pts2 = np.float32([[0,0],[0, height],[width,0],[width,height]])#elde edilmek istenen resmin köşe noktaları


matrix = cv2.getPerspectiveTransform(pts1, pts2)
#1. noktdan 2. noktaya matris geçer
print(matrix)

# nihai dönüştürülmüş resim
#istenen resim=cv2...(resim,matris noktaları,(elde edilmek istenen genişlik yukseklik))
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow("Nihai Resim", imgOutput)