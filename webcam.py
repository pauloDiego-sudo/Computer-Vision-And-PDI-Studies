import cv2

#Para achar cameras online para testar, pesquisar no google:
#      inurl:/mjpg/video.mjpg
# inurl:/mjpg/video.mjpg
# intitle:"Live View / - AXIS"
# inurl:"/view/viewer_index.shtml"
# intitle:"Live NetSnap Cam-Server feed"

#   https://github.com/grigory-lobkov/rtsp-camera-view/issues/3
#rtsp://rtspstream.com/parking
#'http://158.58.130.148/mjpg/video.mjpg'

#Universidade = 'http://tacocam.tacoma.uw.edu/mjpg/video.mjpg'
# camera com movimentos estranhos: http://63.142.183.154:6103/mjpg/video.mjpg
#estacionamento: 'http://view.dikemes.edu.gr/mjpg/video.mjpg'
#Que isso???? http://80.13.189.135/mjpg/video.mjpg
#Cidade: http://77.37.212.198:559/mjpg/video.mjpg

#Praça com pessoas: http://kamera.mikulov.cz:8888/mjpg/video.mjpg
#Praça 2: http://159.130.70.206/mjpg/video.mjpg

#Vila asiática: http://89.106.109.144:12060/mjpg/video.mjpg
#PIER, bom pra saber se tem navio: http://109.247.15.178:6001/mjpg/video.mjpg
#Outro pier: http://94.30.51.166:50000/mjpg/video.mjpg
#Fachada de hotel: http://130.180.105.226:8080/mjpg/video.mjpg?COUNTER
#PRaia: http://212.170.100.189/mjpg/video.mjpg?timestamp=1580392032581
#Kayaks: http://marina.art-net.co.il:140/mjpg/video.mjpg
#Pier in Quebec or France: 'http://doyen-webcam.internet-box.ch:9000/mjpg/video.mjpg'
#Faculdade sei la onde: http://198.160.171.197/mjpg/video.mjpg
#Melhor estacionamento: http://85.202.156.79/mjpg/video.mjpg
#Analog Horror: http://ir3uda.it:8095/view/viewer_index.shtml


#AAAA

webcam = cv2.VideoCapture()
ip = 'http://85.202.156.79/mjpg/video.mjpg'

webcam.open(ip)

while True:
    check,frame = webcam.read()
    img = cv2.resize(frame,(640,420),interpolation=cv2.INTER_AREA) #resizing each frame
    cv2.imshow('WebCam',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #caso a tecla q seja apertada
        break


# #DO COMPUTADOR
# webcamCapture = cv2.VideoCapture(0)
# webcamCapture.set(3,640) #largura é conf 3
# webcamCapture.set(4,420) #altura é conf 4
# webcamCapture.set(10,100) #brilho é conf 10

# while True:
#     check,img = webcamCapture.read()
#     cv2.imshow('WebCam',img)
#     if cv2.waitKey(10) & 0xFF == ord('q'): #caso a tecla q seja apertada
#         break