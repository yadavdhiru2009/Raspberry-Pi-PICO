################################
# timer delay generate With RPi Pico 
# Author: Dharmendra Kumar Yadav
#####################################
from machine import Pin, Timer        #importing pin, and timer class
led= Pin(28, Pin.OUT)              # GPIO14 as led output

led.value(0)              #LED is off
timer=Timer(-1)

timer.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:led.value(not led.value()))   #initializing the timer