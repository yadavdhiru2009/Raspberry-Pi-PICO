################################
# Relay interface with RPi Pico 
# Author: Dharmendra Kumar Yadav
#####################################
from machine import Pin
import time

pin_relay = Pin(0, mode=Pin.OUT)

while True:
    pin_relay.on()
    time.sleep_ms(200)
    pin_relay.off()
    time.sleep_ms(5000)