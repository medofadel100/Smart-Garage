import RPi.GPIO as GPIO
import time
from firebase import firebase

firebase = firebase.FirebaseApplication('https://egy-park-6d3a2-default-rtdb.firebaseio.com/', None)


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG1 = 4
ECHO1 = 17
TRIG2 = 27
ECHO2 = 22
TRIG3 = 5
ECHO3 = 6
TRIG4 = 13
ECHO4 = 19


GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(TRIG4,GPIO.OUT)
GPIO.setup(ECHO4,GPIO.IN)

GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)
GPIO.output(TRIG3, False)
GPIO.output(TRIG4, False)
print ("Calibrating.....")
time.sleep(2)



try:

    count = 0
    while True:
       GPIO.output(TRIG1, True)
       time.sleep(0.00001)
       GPIO.output(TRIG1, False)

       while GPIO.input(ECHO1)==0:
          pulse1_start = time.time()

       while GPIO.input(ECHO1)==1:
          pulse1_end = time.time()

       pulse1_duration = pulse1_end - pulse1_start

       distance1 = pulse1_duration * 17150

       distance1 = round(distance1+1.15, 2)
  
       print ("distance1:",distance1,"cm")
       
       
       GPIO.output(TRIG2, True)
       time.sleep(0.00001)
       GPIO.output(TRIG2, False)

       while GPIO.input(ECHO2)==0:
          pulse2_start = time.time()

       while GPIO.input(ECHO2)==1:
          pulse2_end = time.time()

       pulse2_duration = pulse2_end - pulse2_start

       distance2 = pulse2_duration * 17150

       distance2 = round(distance2+1.15, 2)
       
       print ("distance2:",distance2,"cm")
       
       
       GPIO.output(TRIG3, True)
       time.sleep(0.00001)
       GPIO.output(TRIG3, False)

       while GPIO.input(ECHO3)==0:
          pulse3_start = time.time()

       while GPIO.input(ECHO3)==1:
          pulse3_end = time.time()

       pulse3_duration = pulse3_end - pulse3_start

       distance3 = pulse3_duration * 17150

       distance3 = round(distance3+1.15, 2)
  
       
       print ("distance3:",distance3,"cm")
       
       
       GPIO.output(TRIG4, True)
       time.sleep(0.00001)
       GPIO.output(TRIG4, False)

       while GPIO.input(ECHO4)==0:
          pulse4_start = time.time()

       while GPIO.input(ECHO4)==1:
          pulse4_end = time.time()

       pulse4_duration = pulse4_end - pulse4_start

       distance4 = pulse4_duration * 17150

       distance4 = round(distance4+1.15, 2)
  
       
       print ("distance4:",distance4,"cm")
       
       
       if distance1 <= 3:
              firebase.put('/','/slots/A/ultrasonic','busy')
       if distance1 >= 3:
              firebase.put('/','/slots/A/ultrasonic','free')
       if distance2 <= 3:
              firebase.put('/','/slots/B/ultrasonic','1')
       if distance2 >= 3:
              firebase.put('/','/slots/B/ultrasonic','0')
       if distance3 <= 3:
              firebase.put('/','/slots/C/ultrasonic','1')
       if distance3 >= 3:
              firebase.put('/','/slots/C/ultrasonic','0')
       if distance4 <= 3:
              firebase.put('/','/slots/D/ultrasonic','1')
       if distance4 >= 3:
              firebase.put('/','/slots/D/ultrasonic','0')
        
       count += 1
       if count > 10:
           
            GPIO.cleanup()
            count = 0
            GPIO.setup(TRIG1,GPIO.OUT)
            GPIO.setup(ECHO1,GPIO.IN)
            GPIO.setup(TRIG2,GPIO.OUT)
            GPIO.setup(ECHO2,GPIO.IN)
            GPIO.setup(TRIG3,GPIO.OUT)
            GPIO.setup(ECHO3,GPIO.IN)
            GPIO.setup(TRIG4,GPIO.OUT)
            GPIO.setup(ECHO4,GPIO.IN)
            GPIO.output(TRIG1, False)
            GPIO.output(TRIG2, False)
            GPIO.output(TRIG3, False)
            GPIO.output(TRIG4, False)
            
       time.sleep(2)

except KeyboardInterrupt:
     GPIO.cleanup()
     
     
     
     
     