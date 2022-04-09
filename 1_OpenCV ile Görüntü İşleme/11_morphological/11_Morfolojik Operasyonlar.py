import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("datai_team.jpg",0)#0 siyah beyaz olarak resmi içeri aktarır
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal Img")





#kernel=1 lerden oluşan 5 e 5 lik bir matris ve datatipi integer
kernel = np.ones((5,5), dtype = np.uint8)
#iteration kaç kez erozyon yapılsın
# erozyon :ön plandaki objenin sınırları küçülür
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon")





# genişleme dilation :objenin sınırları genişler
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genisleme")





# white noise gürültü oluşturma
#değişken=np.random...(0,2 arasında(0 dahil 2 degil) random sayı oluştur,boyutu=img.shape[chanel:satır sutun]) resmin boyu kadar chanela ihtiyacımız yok
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255 #0 ve 255 arasında değerle atanr
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("White Noise")





#gürülütü resmin uzerine kendi resmimizi ekleriz
noise_img = whiteNoise + img 
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("Img w White Noise")




# açılma:objenin üzerindeki gürültüyü kaldırır once erozyon sonra genişleme ile
#değişken=cv2.....(resmimiz.integer turunden floata cevrilir,open fonksiyonu kullamılır,kernel verilir)
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Acilma")




# black noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255 #0 dan daha düşük değer aldıgı için siyah alır
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise")

#filtre uygulanır
black_noise_img = blackNoise + img 
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise Img")



# kapatma  :obje üzerindeki noktaciıkları birleştir kğçğk noktalrı yok eder gonce gnişleme sonra erozyon yapılır
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("Kapama")

# gradient :obje uzerindeki genişleme ve erozyon arasındaki farkı verir bize
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradyan")
























