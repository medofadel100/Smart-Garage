import RPi.GPIO as GPIO
import time
import paho.mqtt.client as paho
import os
import socket
import ssl
import random
import string
import json
from time import sleep
from random import uniform
 
connflag = False


def on_connect(client, userdata, flags, rc):                # func for making connection
    global connflag
    print ("Connected to AWS")
    connflag = True
    print("Connection returned result: " + str(rc) )
 
def on_message(client, userdata, msg):                      # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
    
def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str
    
def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]
def getEthName():
  # Get name of the Ethernet interface
  try:
    for root,dirs,files in os.walk('/sys/class/net'):
      for dir in dirs:
        if dir[:3]=='enx' or dir[:3]=='eth':
          interface=dir
  except:
    interface="None"
  return interface
 
#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))
 
mqttc = paho.Client()                                       # mqttc object
mqttc.on_connect = on_connect                               # assign on_connect func
mqttc.on_message = on_message                               # assign on_message func
#mqttc.on_log = on_log

#### Change following parameters #### 
awshost = "a1s6jhl07y2lez-ats.iot.us-west-2.amazonaws.com"      # Endpoint
awsport = 8883                                              # Port no.   
clientId = "Smart-Garage_client"                                     # Thing_Name
thingName = "Smart-Garage_client"                                    # Thing_Name
caPath = "/home/pi/Desktop/AWS/AmazonRootCA1.pem"                                      # Root_CA_Certificate_Name
certPath = "/home/pi/Desktop/AWS/01b12ff894-certificate.pem.crt"                            # <Thing_Name>.cert.pem
keyPath = "/home/pi/Desktop/AWS/01b12ff894-private.pem.key"                          # <Thing_Name>.private.key
 
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  # pass parameters
 
mqttc.connect(awshost, awsport, keepalive=60)               # connect to aws server
 
mqttc.loop_start() 








try:
    while True:
      
      GPIO.setmode(GPIO.BOARD)

      PIN_TRIGGER = 7
      PIN_ECHO = 11
      
      
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
      
      time.sleep(2)
      
      if connflag == True:
        ethName=getEthName()
        ethMAC=getMAC(ethName)
        macIdStr = ethMAC
        
        
        paylodmsg1 = "distance"
        paylodmsg2 = "= "
        paylodmsg3 = "cm"
        
        paylodmsg = "{} {} {} {}".format( paylodmsg1, paylodmsg2, distance, paylodmsg3)
        paylodmsg = json.dumps(paylodmsg) 
        paylodmsg_json = json.loads(paylodmsg)       
        mqttc.publish("Ultrasonic Sensor", paylodmsg_json , qos=1)        # topic: temperature # Publishing Temperature values
        print("msg sent: Ultrasonic Sensor" ) # Print sent temperature msg on console
        print(paylodmsg_json)

    else:
        print("waiting for connection...")

finally:
      GPIO.cleanup()



