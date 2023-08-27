################################
# Potentiometer interface with the RPi Pico
# Author: Dharmendra Kumar Yadav
################################
import machine
import time
 
analog_value = machine.ADC(28)
 
while True:
    reading = analog_value.read_u16()     
    print("ADC: ",reading)
    time.sleep(0.2)