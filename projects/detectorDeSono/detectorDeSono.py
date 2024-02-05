#Esse projeto vai usar o face mesh do mediaPipe
#As aplicações são: Monitoramento de motoristas, Monitoramento de pacientes, Monitoramento de exaustão no trabalho, etc.
import cv2
import mediapipe as mp
import math
import time
import pygame
import threading

dataPath = 'C:/Users/Lenovo/Documents/LAPISCO/ComputerVisionStudies/Computer-Vision-And-PDI-Studies/projects/detectorDeSono/data/'
dataPathLinux = '/home/pdiego/Documentos/Computer-Vision-And-PDI-Studies/projects/detectorDeSono/data/'

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
mpFaceMesh = mp.solutions.face_mesh #carreganndo a solução face mesh
faceMesh = mpFaceMesh.FaceMesh() #Instanciando
mp_drawing = mp.solutions.drawing_utils
inicio = 0
status = "" #Serve para verificar a mudança de status
pygame.mixer.init()
pygame.mixer.music.load(f"{dataPathLinux}e-o-pix-nada-ainda.mp3")

# Function to play the audio
def play_audio():
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.stop()

#Thread para o audio
audio_thread = threading.Thread(target=play_audio)

while video.isOpened():
    check,img = video.read()
    img = cv2.resize(img,(640,480))
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB) #Processando a imagem 
    face_points = results.multi_face_landmarks #Pegando os pontos do rosto
    h,w,_ = img.shape
    
    if results and face_points:
        for face in face_points: #Buscando as coordenadas de faces na imagem
          #  mp_drawing.draw_landmarks(img,face,mpFaceMesh.FACEMESH_FACE_OVAL)
            #Vamos usar os pontos 159 com o 145 para o olho direito, 386 com 374 para o olho esquerdo
            olhoDireitoPontoSuperiorX , olhoDireitoPontoSuperiorY = int(face.landmark[159].x*w) , int(face.landmark[159].y*h) #transformando em pixels
            olhoDireitoPontoInferiorX , olhoDireitoPontoInferiorY = int(face.landmark[145].x*w) , int(face.landmark[145].y*h) #transformando em pixels

            olhoEsquerdoPontoSuperiorX , olhoEsquerdoPontoSuperiorY = int(face.landmark[386].x*w) , int(face.landmark[386].y*h) #transformando em pixels
            olhoEsquerdoPontoInferiorX , olhoEsquerdoPontoInferiorY = int(face.landmark[374].x*w) , int(face.landmark[374].y*h) #transformando em pixels

            # cv2.circle(img,(olhoDireitoPontoSuperiorX,olhoDireitoPontoSuperiorY),1,(255,0,0),2)
            # cv2.circle(img,(olhoDireitoPontoInferiorX,olhoDireitoPontoInferiorY),1,(255,0,0),2)
            # cv2.circle(img,(olhoEsquerdoPontoSuperiorX,olhoEsquerdoPontoSuperiorY),1,(255,0,0),2)
            # cv2.circle(img,(olhoEsquerdoPontoInferiorX,olhoEsquerdoPontoInferiorY),1,(255,0,0),2)

            #Calculando a distancia entre os dois pontos de cada olho
            distDireito = math.hypot(olhoDireitoPontoSuperiorX-olhoDireitoPontoInferiorX,olhoDireitoPontoSuperiorY-olhoDireitoPontoInferiorY)
            distEsquerdo = math.hypot(olhoEsquerdoPontoSuperiorX-olhoEsquerdoPontoInferiorX,olhoEsquerdoPontoSuperiorY-olhoEsquerdoPontoInferiorY)
            
            #Esse valor é fixo para a distancia da camera, portanto deve ser mudado
            if distDireito <= 9 and distEsquerdo <= 9:
                # print('olhos fechados')
                cv2.rectangle(img,(20,60),(260,100),(0,0,255),-1)
                cv2.putText(img,"Olhos fechados",(20,90),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
                situacao = 'F'
                if situacao != status: #So vai iniciar o timer quando houver a mudanca de situacao
                    inicio = time.time() #Cada vez que ele fechar os olhos ele inicia o timer

            else:
                # print('olhos abertos')
                cv2.rectangle(img,(20,60),(250,100),(0,255,0),-1)
                cv2.putText(img,"Olhos Abertos",(20,90),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
                situacao = 'A'
                inicio = time.time() #caso ele abra os olhos, ele reinicia a contagem
                tempo = int(time.time() - inicio)
            
            if situacao == 'F':
                tempo = int(time.time() - inicio)

            status = situacao

            if tempo >= 2:
                cv2.rectangle(img,(20,420),(400,460),(0,0,255),-1)
                cv2.putText(img,f"DORMINDO POR {tempo} SEG",(20,450),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
            if tempo >= 5 and not audio_thread.is_alive():
            # Carregando o arquivo MP3 e executando, tocando o audio com PyGame
                # Start the audio thread
                # Create a thread for audio playback
                audio_thread = threading.Thread(target=play_audio)
                audio_thread.start()
            
    # print("Número de threads ativas:", threading.active_count())
    cv2.imshow('Video',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break