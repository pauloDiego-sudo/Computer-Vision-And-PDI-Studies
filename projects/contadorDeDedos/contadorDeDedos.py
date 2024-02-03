import cv2
import mediapipe as mp

dataPath = 'C:/Users/Lenovo/Documents/LAPISCO/ComputerVisionStudies/Computer-Vision-And-PDI-Studies/projects/contadorDeDedos/'
video = cv2.VideoCapture(0)
# ip = 'http://192.168.1.68:8080/video'
# video.open(ip)

hand = mp.solutions.hands #hand conf
Hand = hand.Hands(max_num_hands=1) #Apenas uma mão será usada
mpDraw = mp.solutions.drawing_utils #Responsável por desenhar os pontos na mão

while video.isOpened():
    check,img = video.read()
    img = cv2.resize(img,(640,480))
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Convertendo para rgb
    results = Hand.process(imgRGB) #Resultados da imagem processada
    handPoints = results.multi_hand_landmarks #extraindo as coordenadas no desenho da mao
    h,w,_ = img.shape #dimensoes da imagem

    pontos = []
    if handPoints: #Se a variavel nao estiver vazia
        for points in handPoints:
            # mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS) #desenhando os pontos da mao
            for id,cord in enumerate(points.landmark): #Para enumenrar os pontos da mao
                cx,cy = int(cord.x*w) , int(cord.y*h) #Transformando as cordenadas landmarks em pixels
                # cv2.putText(img,str(id),(cx,cy+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2) #Colocando o id em cada ponto da mao            
                pontos.append((cx,cy)) #coordenadas dos pontos

        dedos = [8,12,16,20] #com esses pontos, vamos verificar se eles estão abaixos dos outros menores que lees
        contador = 0
        if points: #se a variavel points nao for vazia
            #OBS: MUDAR DE > PARA < PARA REFERENCIAR O DEDAO DA MAO ESQUERDA
            if pontos[4][0] > pontos[2][0]: #para o DEDão, se ele estivar a direita ou a esquerda do ponto 2
                contador+=1

            for d in dedos: #para cada ponto superior
                if pontos[d][1] < pontos[d-2][1]: #Se aquele ponto no eixo Y estiver ACIMA de 2 pontos menores que ele, então ele tá levantado
                    contador += 1
                    #OBS: o eixo Y tem a referencia (0) começando de cima, portanto, a condção IF acima diz "Caso o ponto d esteja acima do ponto d-2"
        
        #deveria ter uma ferramenta dessa nas redes sociais, deveria ter um bando de dados com essas informações para cada região, e assim, quando alguem postar uma foto, deve-ser mostrar um alerta, dizendo que naquela região, o tal simbolo pode ter outro significado
        faction = [2,3,4]
        if contador not in faction:
            cv2.rectangle(img,(20,60),(90,120),(255,0,0),-1)
            cv2.putText(img,str(contador),(20,110),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5)
        elif contador == 2:
            cv2.rectangle(img,(20,20),(50,55),(255,0,0),-1)
            cv2.putText(img,str(contador),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),5)
            cv2.rectangle(img,(20,60),(210,120),(0,0,255),-1)
            cv2.putText(img,"Sinal do CV",(20,110),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),5)
        elif contador == 3:
            cv2.rectangle(img,(20,20),(50,55),(255,0,0),-1)
            cv2.putText(img,str(contador),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),5)
            cv2.rectangle(img,(20,60),(230,120),(0,0,255),-1)
            cv2.putText(img,"Sinal da GDE",(20,110),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),5)
        elif contador == 4:
            cv2.rectangle(img,(20,20),(50,55),(255,0,0),-1)
            cv2.putText(img,str(contador),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),5)
            cv2.rectangle(img,(20,60),(120,120),(0,0,255),-1)
            cv2.putText(img,"Policia",(20,110),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),5)

    cv2.imshow("Imagem",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break