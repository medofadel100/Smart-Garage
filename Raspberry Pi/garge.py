#Libraries
import RPi.GPIO as GPIO
import time
from firebase import firebase

firebase = firebase.FirebaseApplication('https://smart-garage-bbe06-default-rtdb.firebaseio.com/', None)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER_ultr1 = 4
GPIO_ECHO_ultr1 = 17
GPIO_TRIGGER_ultr2 = 4
GPIO_ECHO_ultr2 = 17
GPIO_TRIGGER_ultr3 = 4
GPIO_ECHO_ultr3 = 17
GPIO_TRIGGER_ultr4 = 4
GPIO_ECHO_ultr4 = 17
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_ultr1, GPIO.OUT)
GPIO.setup(GPIO_ECHO_ultr1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_ultr2, GPIO.OUT)
GPIO.setup(GPIO_ECHO_ultr2, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_ultr3, GPIO.OUT)
GPIO.setup(GPIO_ECHO_ultr3, GPIO.IN)
GPIO.setup(GPIO_TRIGGER_ultr4, GPIO.OUT)
GPIO.setup(GPIO_ECHO_ultr4, GPIO.IN)
 


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_ultr1, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_ultr1, False)
 
    StartTime_ultr1 = time.time()
    StopTime_ultr1 = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_ultr1) == 0:
        StartTime_ultr1 = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_ultr1) == 1:
        StopTime_ultr1 = time.time()
 
    # time difference between start and arrival
    TimeElapsed_ultr1 = StopTime_ultr1 - StartTime_ultr1
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance1 = (TimeElapsed_ultr1 * 34300) / 2
    
     # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_ultr2, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_ultr2, False)
 
    StartTime_ultr2 = time.time()
    StopTime_ultr2 = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_ultr2) == 0:
        StartTime_ultr2 = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_ultr2) == 1:
        StopTime_ultr2 = time.time()
 
    # time difference between start and arrival
    TimeElapsed_ultr2 = StopTime_ultr2 - StartTime_ultr2
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance2 = (TimeElapsed_ultr2 * 34300) / 2
    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_ultr3, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_ultr3, False)
 
    StartTime_ultr3 = time.time()
    StopTime_ultr3 = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_ultr3) == 0:
        StartTime_ultr3 = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_ultr3) == 1:
        StopTime_ultr3 = time.time()
 
    # time difference between start and arrival
    TimeElapsed_ultr3 = StopTime_ultr3 - StartTime_ultr3
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance3 = (TimeElapsed_ultr3 * 34300) / 2
    
    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_ultr4, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_ultr4, False)
 
    StartTime_ultr4 = time.time()
    StopTime_ultr4 = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_ultr4) == 0:
        StartTime_ultr4 = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_ultr4) == 1:
        StopTime_ultr4 = time.time()
 
    # time difference between start and arrival
    TimeElapsed_ultr4 = StopTime_ultr4 - StartTime_ultr4
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance4 = (TimeElapsed_ultr4 * 34300) / 2
    
    
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            
            distance()
            print ("Measured Distance1 = %.1f cm" % distance1)
            
            if dist1 <= 50:
              firebase.put('/','/Garage%20Slot%201%20ultrasonic','1')
            if dist1 >= 50:
              firebase.put('/','/Garage%20Slot%201%20ultrasonic','0')
            time.sleep(1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()