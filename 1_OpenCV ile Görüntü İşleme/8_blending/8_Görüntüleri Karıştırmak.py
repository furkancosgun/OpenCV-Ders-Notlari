import cv2
import matplotlib.pyplot as plt

#goruntuler eklenir
img1 = cv2.imread("img1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#goruntule gosterilir
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#koşeler alınır
print(img1.shape)
print(img2.shape)

#yeni koşeler atanır
img1 = cv2.resize(img1, (600,600))
print(img1.shape)

img2 = cv2.resize(img2, (600,600))
print(img2.shape)

#yeni koşe atanmış goruntu gosterilir
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# karıştırılmış resim = alpha*img1 + beta*img2 
 #alpha ve beta goruntunun saydamlıgıdır
blended = cv2.addWeighted(src1 = img1, alpha =0.5, src2= img2, beta = 0.5, gamma = 0)
plt.figure()
plt.imshow(blended)















