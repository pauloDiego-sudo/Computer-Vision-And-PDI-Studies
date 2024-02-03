import cv2
#Files path
imgPath = 'data/farol.jpg'
impathh = 'processedata/'

#CORTAR IMAGEM
img =  cv2.imread(imgPath)
regionOfinterest = cv2.selectROI('Selecionando ROI',img,False)
imgprocessedName = input('Digite o nome da imagem: ')
cv2.destroyWindow('Selecionando ROI')
x1 = int(regionOfinterest[1])
x2 = x1+int(regionOfinterest[3])
y1 = int(regionOfinterest[0])
y2 = y1+int(regionOfinterest[2])
#farol: y = 310 à 520 : x = 120 à 420
recorte = img[x1:x2,y1:y2]
# cv2.imshow('Imagem',img)
cv2.imwrite(f'{impathh}{imgprocessedName}.jpg',recorte)
cv2.waitKey(0)


# ABRIR IMAGEM

# img = cv2.imread(imgPath) #Read the image
# imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) #converting RGB to Gray scale
# cv2.imshow('Imagem Cinza',imgGray) 
# cv2.imshow('Imagem',img) #Show the image on the screen
# cv2.waitKey(0) #Locks the window to show the image (otherwise it will display and close automaticaly)

# print(img.shape) #It display tuple (height,width,channels)