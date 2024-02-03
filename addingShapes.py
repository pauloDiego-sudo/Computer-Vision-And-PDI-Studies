import cv2

video = cv2.VideoCapture('data/runners.mp4')

while True:
    check,frame = video.read()
    cv2.rectangle(frame,(50,50),(200,200),(255,0,0),5)
    cv2.circle(frame,(300,300),80,(0,0,255),5)
    cv2.line(frame,(300,300),(380,300),(255,255,0),2)

    texto = "Corredores e formas"
    cv2.putText(frame,texto,(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(100,255,180),2)
    cv2.imshow('Corredores',frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
    