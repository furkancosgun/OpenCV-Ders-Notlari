import cv2
import numpy as np
from collections import deque

# nesne merkezini depolayacak veri tipi
buffer_size = 16#depolama boyutu 16
pts = deque(maxlen = buffer_size)#merkez nokta point uzunlguu depo boyutu kadar olsun

# mavi renk aralığı HSV
blueLower = (84,  98,  0)#mavi rengin max degeri
blueUpper = (179, 255, 255)#mavi rengin min degeri
            #renk,doygunluk,parlaklık
# capture
cap = cv2.VideoCapture(0)
cap.set(3,960)
cap.set(4,480)

while True:
    
    success, imgOriginal = cap.read()
    if cv2.waitKey(1) & 0xFF == ord("q"): break
    
    if success: 
        
        # blur =gaussian(image,(k size),standart sapma x ve y  degerlerinde)
        blurred = cv2.GaussianBlur(imgOriginal, (11,11), 0) 
        
        
        # hsv    / bgr dan hsv formatına cevrilir
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        cv2.imshow("HSV Image",hsv)
        
        
        # mavi için maske oluştur
        #hsv=degerarasinda(hsv için,min deger ,max deger)
        mask = cv2.inRange(hsv, blueLower, blueUpper)
        cv2.imshow("mask Image",mask)
        # maskenin etrafında kalan gürültüleri sil
        mask = cv2.erode(mask, None, iterations = 2)#erozyon
        mask = cv2.dilate(mask, None, iterations = 2)#genişleme
        cv2.imshow("Mask + erozyon ve genisleme",mask)
        
        # farklı sürüm için
        # (_, contours,_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # kontur
        #tuple(contour al,boş geç)=contourbul(mask.copyala bozma,external dış kontour bul,kontourleri sadece koşelerden al )
        (contours,_) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None
        #merkez boje
        
        
        if len(contours) > 0:#eger kontour var ise
            
            # en buyuk konturu al
            #c ye ata=en buyu(contourler içinden,kontor alanından en buygunu)
            c = max(contours, key = cv2.contourArea)
            
            # dikdörtgene çevir 
            #contourler içinden minimum alana sahip dikdortgen dondurur
            rect = cv2.minAreaRect(c)
            
            #rect bi tuple oldugu için değişkenlere atıyoryz degerleri
            ((x,y), (width,height), rotation) = rect
            
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            print(s)
            
            # kutucuk
            box = cv2.boxPoints(rect)
            box = np.int64(box)
            
            # moment
            M = cv2.moments(c)
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))
            
            # konturu çizdir: sarı
            #contor cizdir(resme,[kutuckdaki x y],yarıçap,renk,kalınlık)
            cv2.drawContours(imgOriginal, [box], 0, (0,255,255),2)
            
            
            # merkeze bir tane nokta çizelim: pembe
            #daire(resim,merkeze,yarıçap,renk,doldur)
            cv2.circle(imgOriginal, center, 5, (255,0,255),-1)
            
            
            # bilgileri ekrana yazdır
            #yazıekle(resme,text,(x ve y),font,1,renk,kalınlık)
            cv2.putText(imgOriginal, s, (25,50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 2)
            
            
        # deque
        #takip hafıazsı
        #points.ekle(merkez)
        pts.appendleft(center)
        #1 ile kaç nokta varsa içinde dön
        for i in range(1, len(pts)):
            
            #noktanın bir onceki indexi box işe noktanın o anki indexi boş ise :devam
            if pts[i-1] is None or pts[i] is None: continue
        
        
            #cv2.çizgi(resme,bir onceki point,anlık point,(renk),kalınlık)
            cv2.line(imgOriginal, pts[i-1], pts[i],(0,255,0),3) # 
            
        cv2.imshow("Orijinal Tespit",imgOriginal)
        
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
