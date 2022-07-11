from pyzbar import pyzbar
import cv2
from gpiozero import *
from time import sleep

#GPIO Configeration 
sensor= DistanceSensor(echo=14,trigger=15,max_distance=1)
red = LED(27)
green = LED(22)
servo = Servo (4)

red.off()
green.off()

servo.min()

cap =cv2.VideoCapture(0)

def scan():
    global frame
    Bool,frame =cap.read()    
    Barcodes = pyzbar.decode(frame)
    for code in Barcodes:
        (x,y,w,h)=code.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        barcodeData= code.data.decode("utf-8")
        cv2.putText(frame,barcodeData,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0.255),2)
        return  barcodeData
while True:
    ScanerValue = scan()
    if ScanerValue == 'enter':
        servo.max() 
        sleep(1)
    else:
        servo.min()
    dis_cm=sensor.distance*100
    print(dis_cm)
    if dis_cm < 10:
        green.on()
        red.off()
    else :
        red.on()
        green.off()
    cv2.imshow('scan',frame)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()
