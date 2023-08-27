################################
# Ultrasonic Snsor Ditance Measurment With RPi Pico 
# Author: Dharmendra Kumar Yadav
#####################################
from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=2, echo_pin=3, echo_timeout_us=10000)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)