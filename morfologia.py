import cv2
#Porquê aplicar blur? O blur serve para suavizar a imagem para a detecção de formas
#Opening = Erosão -> Dilatação (Serve Para tirar os ruídos da imagem toda)
#Closening = Dilatação -> Erosão (Serve para tirar os ruídos de dentro dos objetos )

img = cv2.imread('data/piramide.jpg')
imgOriginal = cv2.resize(img,(500,400)) #resizing
imgCinza = cv2.cvtColor(imgOriginal,cv2.COLOR_RGB2GRAY) #Gray image
imgBlur = cv2.GaussianBlur(imgCinza,(7,7),0) #Blured image kernel 7x7
imgCanny = cv2.Canny(imgOriginal,50,100) #Aplicando o filtro de Canny
imgDilat = cv2.dilate(imgCanny,(5,5),iterations=2) #Expands the object with kernel 5x5, greater the iterations, greater dilatation
imgErode = cv2.erode(imgCanny,(5,5),iterations=2) #Erodes the image, desfragments it
imgOpening1 = cv2.morphologyEx(imgCanny,cv2.MORPH_OPEN,(5,5)) #Built in opening algortihm
imgOpening2 = cv2.dilate(imgErode,(5,5)) #Erode - > dilat
imgClosening1 = cv2.morphologyEx(imgCanny,cv2.MORPH_CLOSE,(5,5)) #Built in Closening algortihm
imgClosening2 = cv2.erode(imgDilat,(5,5)) #Dilat -> erode

# cv2.imshow('Original',imgOriginal)
# cv2.imshow('Cinza ',imgCinza)
# cv2.imshow('Blur Cinza ',imgBlur)
cv2.imshow('Canny ',imgCanny)
# cv2.imshow('Dilatation ',imgDilat)
# cv2.imshow('Erode',imgErode)
cv2.imshow('OP 1',imgOpening1)
cv2.imshow('OP 2',imgOpening2)
cv2.imshow('CL 1',imgClosening1)
cv2.imshow('CL 2',imgClosening2)

cv2.waitKey(0)