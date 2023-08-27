################################
# Button interface with the RPi Pico
# Author: Dharmendra Kumar Yadav
################################
from machine import Pin
import time

led = Pin(16, Pin.OUT) #set GP16 as OUTPUT pin
button = Pin(14, Pin.IN,Pin.PULL_DOWN) #set GP14 as OUTPUT pin

while True:
    if button.value():
        print("Button is pressed!")
        led.toggle()
        time.sleep(0.5)