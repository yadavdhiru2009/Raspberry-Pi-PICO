################################
# Infra red Sensor Module interface with RPi Pico 
# Author: Dharmendra Kumar Yadav
#####################################
import machine
import utime
reed = machine.Pin(16, machine.Pin.IN)
led = machine.Pin(17, machine.Pin.OUT)
while True:
    if reed.value() == 0:
        led.value(0)
        print("IR Sensor Detected!")
        utime.sleep(1)
        led.value(0)