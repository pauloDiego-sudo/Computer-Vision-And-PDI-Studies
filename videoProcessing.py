import cv2
#Files path
imgPath = 'data/farol.jpg'
videoPath = 'data/runners.mp4'

video = cv2.VideoCapture(videoPath) #Captura o video

while True: #Um video é uma sequencia de imagens
    check,img = video.read() #Lê o video frame a frame
    imgRedimencionada = cv2.resize(img,(640,420)) #Imagem redimensionada
    cv2.imshow('Video Window',imgRedimencionada) #Mostra o video, nesse caso, cada imagem
    cv2.waitKey(10) #Every 10 loops, it goes to the next frame

    #print(img.shape) #It display tuple (height,width,channels)