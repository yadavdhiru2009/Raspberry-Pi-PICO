################################
# PIR sensor interface with the RPi Pico
# Author: Dharmendra Kumar Yadav
################################
from machine import Pin #import Pin library
from time import sleep # import sleep function

buzzer = Pin(15, Pin.OUT,Pin.PULL_UP) #set GP15 as digital output pin for buzzer
pir = Pin(16, Pin.IN,Pin.PULL_DOWN)  # set GP16 as digital input pin for PIR motion sensor

while True:
    if pir.value(): #when PIR detects motion 
        print("Intruder is detected!")  
        buzzer.low() # make buzzer alarm
        
    else:
        buzzer.high() #close buzzer alarm
        print("No Intruder!")
    sleep(0.1)