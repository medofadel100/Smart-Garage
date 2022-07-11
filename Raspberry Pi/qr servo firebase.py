import cv2
import time
import numpy as np
#import RPi.GPIO as GPIO
from firebase import firebase
firebase = firebase.FirebaseApplication('https://egy-park-6d3a2-default-rtdb.firebaseio.com/', None)
# set up camera object
cap = cv2.VideoCapture(0)

# QR code detection object
detector = cv2.QRCodeDetector()

#import RPi.GPIO as GPIO
import time
#GPIO.setmode(GPIO.BCM)
#servo_pin = 4
#GPIO.setup(servo_pin,GPIO.OUT)

#pwm = GPIO.PWM(servo_pin,50) # 50 Hz (20 ms PWM period)

#pwm.start(7) # start PWM by rotating to 90 degrees
while True:
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    
    # if there is a bounding box, draw one, along with the data
    if(bbox is not None):
        # for i in range(len(bbox)):
        #     cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255,
        #              0, 255), thickness=2)
        # cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX,
        #             0.5, (0, 255, 0), 2)
        if data:
            print("data found: ", data)
            
            
            email,Slote= data.split(',')
            
            print("email: ", email)
            print("slote: ", Slote)
            
            if Slote == 'A':
                #result = firebase.put("/", "/Garage%20gate/Enter%20gate", "90")
               # pwm.ChangeDutyCycle(7.0) # rotate to 90 degrees
                #time.sleep(2)
                
                print ("open Enter gate")
                result = firebase.put("/", "/slots/A/gate", "open")
                print ("open gate A ")
               # print ("close Enter gate")
               # pwm.ChangeDutyCycle(2.0) # rotate to 0 degrees
            
            
                
            if Slote == 'B':
                print ("open Enter gate")
                #result = firebase.put("/", "/Garage%20gate/Enter%20gate", "90")
                #time.sleep(60)
                print ("open Enter gate")
                result = firebase.put("/", "/slots/B/gate", "open")
                print ("open gate B ")
               # print ("close Enter gate")
                
                
                
            if Slote == 'C':
                #result = firebase.put("/", "/Garage%20gate/Enter%20gate", "90")
                #time.sleep(60)
                print ("open Enter gate")
                result = firebase.put("/", "/slots/C/gate", "open")
                print ("open gate C ")
                #print ("close Enter gate")
                time.sleep(0.2)
                
            if Slote == 'D':
                #result = firebase.put("/", "/Garage%20gate/Enter%20gate", "90")
                #time.sleep(60)
                print ("open Enter gate")
                result = firebase.put("/", "/slots/D/gate", "open")
                print ("open gate D ")
                #print ("close Enter gate")
                time.sleep(0.2)
                
    # display the image preview
    cv2.imshow("code detector", img)
    if(cv2.waitKey(1) == ord("q")):
        break
# free camera object and exit
cap.release()
cv2.destroyAllWindows()
