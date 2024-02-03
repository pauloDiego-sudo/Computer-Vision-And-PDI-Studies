import cv2

img1 = cv2.resize(cv2.imread('data/img02.jpg'),(600,700))
img1Cinza = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
_,th1 = cv2.threshold(img1Cinza,127,255,cv2.THRESH_BINARY) #Threshold binário simples
th2 = cv2.adaptiveThreshold(img1Cinza,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,16) #Threshold binário adaptative gausiano, com blocksize
#O BLOCK SIZE DEVE SER ACHADO NA TENTATIVA E ERRO
th3 = cv2.adaptiveThreshold(img1Cinza,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,16)

# cv2.imshow('Original',img1)
cv2.imshow('Threshold Binario',th1)
cv2.imshow('Threshold Binario Adaptativo Gausiano',th2)
cv2.imshow('Threshold Binario Adaptativo Mean',th3)
cv2.waitKey(0)