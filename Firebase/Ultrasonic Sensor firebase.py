import RPi.GPIO as GPIO
from time import sleep
from firebase import firebase
import time

firebase = firebase.FirebaseApplication('https://smart-garage-bbe06-default-rtdb.firebaseio.com/', None)
firebase.put("/", "/Garage%20Slot%201%20ultrasonic", "0")


try:
    while True:
      
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 4
      PIN_ECHO = 17
      
      
      GPIO.setup(PIN_TRIGGER, GPIO.OUT)
      GPIO.setup(PIN_ECHO, GPIO.IN)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      print ("Waiting for sensor to settle")

      time.sleep(2)

      print ("Calculating distance")

      GPIO.output(PIN_TRIGGER, GPIO.HIGH)

      time.sleep(0.00001)

      GPIO.output(PIN_TRIGGER, GPIO.LOW)

      while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time() 
      while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time() 

      pulse_duration = pulse_end_time - pulse_start_time
      distance = round(pulse_duration * 17150, 2)
      print ("Distance:",distance,"cm")
      if distance <= 5:
            firebase.put("/", "/slot/", "1")
      if distance >= 5:
            firebase.put("/", "/Garage%20Slot%201%20ultrasonic", "0")      
finally:
      GPIO.cleanup()

