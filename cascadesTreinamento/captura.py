import cv2

celphoneCameraIP = 'http://192.168.1.68:8080/video'
camera = cv2.VideoCapture(celphoneCameraIP)

amostra = 1
while True:
    check,img = camera.read()
    imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    if cv2.waitKey(1) & 0xFF == ord('s'):  #Para salvar a imagem toda vez que apertar "s"
        imgR = cv2.resize(imgCinza,(220,220))
        cv2.imwrite(f'photos/p/im{amostra}.jpg',imgR)
        amostra += 1

    cv2.imshow('Webcam',cv2.resize(img,(600,500)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
