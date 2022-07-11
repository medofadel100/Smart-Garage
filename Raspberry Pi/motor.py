import RPi.GPIO as gpio
import time
def init():    
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)

def forward(sec):
    init()
    gpio.output(17, False)
    gpio.output(22, True)

    time.sleep(sec)
    gpio.cleanup() 
def reverse(sec):
    init()
    gpio.output(17, True)
    gpio.output(22, False)

    time.sleep(sec)
    gpio.cleanup()
def left_turn(sec):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    time.sleep(sec)
    gpio.cleanup()
def right_turn(sec):
    init()
    gpio.output(17, False)
    gpio.output(22, True)

    time.sleep(sec)
    gpio.cleanup()
seconds = 3
time.sleep(seconds)
print("forward")
forward(seconds)
time.sleep(seconds-2)
print("right")
right_turn(seconds)
time.sleep(seconds-2)
time.sleep(seconds)
print("forward")
forward(seconds)
time.sleep(seconds-2)
print("right")
right_turn(seconds)
time.sleep(seconds-2)