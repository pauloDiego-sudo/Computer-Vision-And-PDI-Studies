#Usaremos o MediaPipe, que é do google, e tras diversas soluções em IA, nesse projetos usaremos o Pose, pra mapear o corpo humano

import cv2
import mediapipe as mp
import math

dataPath = 'C:/Users/Lenovo/Documents/LAPISCO/ComputerVisionStudies/Computer-Vision-And-PDI-Studies/projects/contadorDePolichinelos/data/'

video = cv2.VideoCapture(f'{dataPath}poli.mp4')
pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence=0.5,min_detection_confidence=0.5) #Variável de detecção
draw = mp.solutions.drawing_utils  #Variável para desenhar as linhas e pontos no video
menorDistMaos = set()
maiorDistPes = set()
contador_polichinelos = 0
check_polichinetlo = True #Para contabilizar so uma vez

while video.isOpened():
    check,frame = video.read()
    img = cv2.resize(frame,(640,420),interpolation=cv2.INTER_AREA) #resizing each frame
    videoRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Transforma a img para RGB
    
    results = Pose.process(videoRGB) #Processa a imagem e devolve os pontos do corpo
    points = results.pose_landmarks #Pontos do conpo
    draw.draw_landmarks(img,points,pose.POSE_CONNECTIONS) #Desenha os pontos e suas conexões no frame da imagem
    #OBS: Verificar na documentação do MEDIAPIPE, quais pontos pegar para fazer a distancia entre eles
    #Nesse caso vamos usar os pontos 19 (mão esquerda), 20 (mão direita), 31 (pé esquerdo) e 32 (pé direito)

    h,w,_ = img.shape #Extraindo as dimensões da imagem

    if points: #Caso points não esteja vazia
        #PRECISAMOS EXTRAIR AS COORDENADAS X E Y DOS PES E MAOS, e transformar em pixels multiplicando y por h, e x por w
        peDireitoY = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].y*h)
        peDireitoX = int(points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX].x*w)

        peEsquerdoY = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].y*h)
        peEsquerdoX = int(points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX].x*w)

        maoDireitaY = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].y*h)
        maoDireitaX = int(points.landmark[pose.PoseLandmark.RIGHT_INDEX].x*w)
        
        maoEsquerdaY = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].y*h)
        maoEsquerdaX = int(points.landmark[pose.PoseLandmark.LEFT_INDEX].x*w)

        #Precisamos calcular a distancia entre os pontos
        distMaos = math.hypot(maoDireitaX-maoEsquerdaX,maoDireitaY-maoEsquerdaY) #Distancia entre as duas maos calculada pela hipotenusa
        distPes = math.hypot(peDireitoX-peEsquerdoX,peDireitoY-peEsquerdoY)

        #Devemos experimentalmente achar a menor distancia entre as mãos e a maior distancia entre os pes
        # maiorDistPes.add(distPes)
        # menorDistMaos.add(distMaos)
        # print(f'maos {distMaos} pes {distPes}')
        #No meu caso, a menor distancia media entre as maos é 55, e a maior media entre os pes é 80

        if check_polichinetlo == True and distMaos <= 55 and distPes >= 80:
            contador_polichinelos+=1
            check_polichinetlo = False #Caso a variavel check esteja true, ele seta falso até o polichinelo ser desfeito
        #Para não contabilizar o mesmo valor duas vezes
            
        if distMaos > 55 and distPes < 80:
            check_polichinetlo = True

        texto = f"QTD = {contador_polichinelos}"
        cv2.rectangle(img,(25,60),(180,120),(255,0,0),-1)
        cv2.putText(img,texto,(30,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),5)

    cv2.imshow('Video',img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
