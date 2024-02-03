import cv2

imgPath = 'C:/Users/Lenovo/Documents/LAPISCO/ComputerVisionStudies/Computer-Vision-And-PDI-Studies/data/objetos.jpg'
imgSavePath = 'C:/Users/Lenovo/Documents/LAPISCO/ComputerVisionStudies/Computer-Vision-And-PDI-Studies/processedata/objetos/'
img = cv2.resize(cv2.imread(imgPath),(600,500))
imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#extraindo contornos
imgCanny = cv2.Canny(imgCinza,30,200)



#Aplicando a morfologia closing, para o algoritmo ficar mais preciso
imgClose = cv2.morphologyEx(imgCanny,cv2.MORPH_CLOSE,(7,7))

#Achando os contornos
contours,hierarchy = cv2.findContours(imgClose,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #O modo é como o algoritmo vai procurar os contornos, no caso, o retr external é para contornos  que fecham o objeto

#Desenhando e separando os contornos
numObjeto = 1
for contour in contours:
    # cv2.drawContours(img,contour,-1,(255,0,0),2) #Desenhando os contornos para cada objeto encontrado
    x,y,w,h = cv2.boundingRect(contour) #Extraindo os atributos dos contornos encontrados
    objeto = img[y:y+h,x:x+w] #Encontrando o objeto na imagem
    # cv2.imwrite(f'{imgSavePath}{numObjeto}.jpg',objeto) #Salvando o objeto
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #Desenhando as boundie boxes
    numObjeto+=1


cv2.imshow('IMG original',img)
cv2.imshow('IMG Closed',imgClose)
cv2.waitKey(0)