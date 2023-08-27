################################
#Analog joystick interface With RPi Pico 
# Author: Dharmendra Kumar Yadav
#####################################
import tm1637
from machine import Pin
from utime import sleep

display = tm1637.TM1637(clk=Pin(26), dio=Pin(27))
 
# Word
display.show("DAbC")
sleep(1)
 
#Clear all
display.show("    ")
sleep(1)
 
#Numbers
display.number(1234)
sleep(1)
 
#Time with colon
display.numbers(10,40)
sleep(1)
 
#Lower Brightness
display.brightness(0)
sleep(1)
 
#Scrolling text
display.scroll("SCrOLL", delay=500)
sleep(1)
 
#Temperature
display.temperature(37)
sleep(1)
 
#Clear all
display.show("    ")