import cv2
import matplotlib.pyplot as plt

# template matching: sablon esleme

img = cv2.imread("cat.jpg", 0)#ana resim
print(img.shape)
template = cv2.imread("cat_face.jpg", 0)#resimden kesilen şablon
print(template.shape)
h, w = template.shape

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
        
    
    #eval stringden fonksiyona çevirir
    method = eval(meth) # 'cv2.TM_CCOEFF' -> cv2.TM_CCOEFF
    
    res = cv2.matchTemplate(img, template, method)
                #resim,template,method
                
                
    print(res.shape)
    
    
    
    #çıkan sonucun min max degerini atar
    #location ve degerlerini atar
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    
    
    #
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc#yukarıdaki fonksiyonların locationu farklı
    else:
        top_left = max_loc
    
    
    
    #alt sag=(sol yukarı[0.indexi])+yuksekilk,sol yukarının[1.indexi]+genişlik
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    
    #dikdortgen oluştur (resim ,sol yukarıdan,sag alta kadar,renk,kalınlık) şablon ile eşleşen kısım
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    
    plt.figure()
    plt.subplot(121), plt.imshow(res, cmap = "gray")
    plt.title("Eşleşen Sonuç"), plt.axis("off")
    plt.subplot(122), plt.imshow(img, cmap = "gray")
    plt.title("Tespit edilen Sonuç"), plt.axis("off")
    plt.suptitle(meth)
    
    plt.show()
    
    
    
 
    
    
    
    