################################
# TMP36 temperature sensor Tests on the RPi Pico
# Author: Dharmendra Kumar Yadav
################################
#
from machine import ADC
from time import sleep

adcpin = 26
tmp36 = ADC(adcpin)

while True:
    adc_value = tmp36.read_u16()
    volt = (3.3/65535)*adc_value
    degC = (100*volt)-50
    print(round(degC, 1))
    sleep(5)