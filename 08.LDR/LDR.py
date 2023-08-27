################################
# LDR(Light Dependent Resistor )interface with the RPi Pico
# Author: Dharmendra Kumar Yadav
################################
from machine import Pin, PWM, ADC #import Pin, PWM, ADC handling library

pwm = PWM(Pin(15)) #Pico GP15 is a PWM output pin
adc = ADC(Pin(28)) #Pico GP28 is a ADC analog input pin

pwm.freq(1000) #set PWM frequency at 1000 hz

while True:
    duty = adc.read_u16() #read  Light intensity
    pwm.duty_u16(60000-duty) #provide current to LED, the more light intensity, the less current to LED