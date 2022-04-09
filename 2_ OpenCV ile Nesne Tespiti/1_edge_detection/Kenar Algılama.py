import cv2
import matplotlib.pyplot as plt
import numpy as np

# resmi içe aktar
img = cv2.imread("london.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off")

edges = cv2.Canny(image = img, threshold1 = 0, threshold2 = 255)#thershold1=en duşuk,thers2=en buyuk
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")

med_val = np.median(img)#median degeri gorseldeki veri skalasını küçükten buyuge sıralandıgında ortadan ikiye ayıran değere denir.
print(med_val)

low = int(max(0, (1 - 0.33)*med_val)) #median degerini %67 sini alır
high = int(min(255, (1 + 0.33)*med_val))#median degerinin %33 unu alır

print(low)
print(high)

edges = cv2.Canny(image = img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")

# blur
blurred_img = cv2.blur(img, ksize = (5,5))
plt.figure(), plt.imshow(blurred_img, cmap = "gray"), plt.axis("off")

med_val = np.median(blurred_img)
print(med_val)

low = int(max(0, (1 - 0.33)*med_val))
high = int(min(255, (1 + 0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image = blurred_img, threshold1 = low, threshold2 = high)
plt.figure(), plt.imshow(edges, cmap = "gray"), plt.axis("off")




















