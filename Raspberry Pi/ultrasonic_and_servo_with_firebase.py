#Libraries
import RPi.GPIO as GPIO
import time
from firebase import firebase

firebase = firebase.FirebaseApplication('https://egy-park-6d3a2-default-rtdb.firebaseio.com/', None)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER = 4
GPIO_ECHO = 17
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


servo_gate1_pin = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_gate1_pin,GPIO.OUT)
            
# setup PWM process
pwm_gate1 = GPIO.PWM(servo_gate1_pin,50) # 50 Hz (20 ms PWM period)
#set GPIO Pins



def distance():
    # set Trigger to HIGHN
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    
    
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            
            
            
            pwm_gate1.start(7) # start PWM by rotating to 90 degrees
            gate1 = firebase.get('/slots/A/gate','')
            print (gate1)

            if gate1 == 0 :
                pwm_gate1.ChangeDutyCycle(2.0) # rotate to 0 degrees
                time.sleep(3)
                
            if gate1 == 90 :
                pwm_gate1.ChangeDutyCycle(7.0) # rotate to 90 degrees
                time.sleep(3)
                
            if gate1 == 180 :
                pwm_gate1.ChangeDutyCycle(12.0) # rotate to 180 degrees
                time.sleep(3)
            
            
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            
            if dist <= 50:
              firebase.put('/','/slots/A/State','busy')
            if dist >= 50:
              firebase.put('/','/slots/A/State','free')
            time.sleep(1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()