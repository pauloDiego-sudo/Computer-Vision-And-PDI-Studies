import cv2
import pickle
import numpy as np

dataPath = 'C:/Users/Lenovo/Documents/LAPISCO/ComputerVisionStudies/Computer-Vision-And-PDI-Studies/projects/contadorDeVagas/data/'

vagas = []

with open(f'{dataPath}vagas.pkl','rb') as arquivo: #Escrevendo as coordenadas das vagas do arquivo para o array
    vagas = pickle.load(arquivo)

video = cv2.VideoCapture(f'{dataPath}video.mp4') #video

while video.isOpened(): #Enquanto o video estiver rodando
    check, img = video.read()
    imgCinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #frames cinzas
    imgTh = cv2.adaptiveThreshold(imgCinza,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16) #Threshold adaptativo, onde é branco fica preto e vice-versa
    #Para saber se o carro está na vaga, vamos identificar a itensidade de cores brancas na vaga
    imgMedian = cv2.medianBlur(imgTh,5) #Para limpar o threshold
    kernel = np.ones((3,3),np.int8) #Matriz de 1's de tamanho 3x3
    imgDilat = cv2.dilate(imgMedian,kernel) #Expandindo os pixels para melhoras a detecção

    vagasLivres = 0 
    for x,y,w,h in vagas: #To place the rectangles
        vaga = imgDilat[y:y+h,x:x+w] #Cada retangulo de cada vaga
        count = cv2.countNonZero(vaga) #Vai calcular a quantidade de pixels NÃO zero, ou seja , brancos, dentro de cada vaga
        #cv2.putText(img,str(count),(x,y+h-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255)) #Quantidades de pixels brancos em cada vaga

        #Podemos observar que acima de 900 pixels brancos, existe carro na vaga
        if count < 900: #Quando tiver uma intensidade de brancos menor que 900, não há carro
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) #Colocando os retangulos nas coordenadas
            vagasLivres+=1 #Incrementa o contador devagas
        else: #Existe carro na vaga
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) #Colocando os retangulos nas coordenadas

        cv2.rectangle(img, (90,0),(415,60),(0,255,0),-1) #Retangulo atras do texto
        cv2.putText(img,f'LIVRES: {vagasLivres}/69',(95,45),cv2.FONT_HERSHEY_SIMPLEX,1.2,(255,255,255),5) #Texto

    cv2.imshow('Video',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

