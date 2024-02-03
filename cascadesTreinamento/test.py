# O método de treinamento haarcascade funciona assim:
# -Pegamos várias imagens de um objetos que queremmos, e daremos como POSITIVO
# -Pegamos várias imagens de um objetos que não queremmos, e daremos como NEGATIVO
# Assim o algoritmo extrai caracteristicas iguais do mesmo objeto
# No final temos um XML para ser usado

# DESVANTAGENS: Muitos falsos positivos

import cv2

celphoneCameraIP = 'http://192.168.1.68:8080/video'
camera = cv2.VideoCapture(celphoneCameraIP)
cascadesPath = 'C:/Users/Lenovo/Documents/LAPISCO/ComputerVisionStudies/PractialCourse/cascadesTreinamento/photos/classifier/'
classificador = cv2.CascadeClassifier(f'{cascadesPath}cascade.xml')

while True:
    check,img = camera.read()
    imgCinza = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY) #A imagem cinza so serve para passar como parametro para o classificador
    objetos = classificador.detectMultiScale(imgCinza,scaleFactor=1.2) #detecta o objeto dentro da imagem e retorna as coordenadas do objeto, a minSize é em pixels
    if len(objetos) == 0:
        pass
    if len(objetos) != 0:
        for x,y,w,h in objetos:  #Extraindo as coordenadas e desenhando as boundie boxes
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #Desenhando as boundie boxes

    cv2.imshow("Webcam",cv2.resize(img,(500,400)))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break 