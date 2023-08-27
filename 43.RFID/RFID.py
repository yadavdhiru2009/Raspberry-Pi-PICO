################################
# RFID interface with the RPi Pico
# Author: Dharmendra Kumar Yadav
"""
Pico Pins      RFID Pins
GP5            SDA
GP6            SCK
GP7            MOSI
GP4            MISO
 -               IRQ
GND            GND
GP18           RST
3.3V           3.3V
***********************************************
Pico Pins      Devices
GP14           Red LED through 220ohm resistor
GP15           Green LED through 220ohm resistor
GP16           Buzzer I/O pin

"""
################################
import time
from machine import I2C, Pin, SPI #import I2C,Pin,SPI library
from mfrc522 import MFRC522 #import RFID reader library
buzzer= Pin(16, Pin.OUT) #set buzzer to GP16
buzzer.value(1)
true = Pin(15, Pin.OUT)  #set Green LED to GP15
false = Pin(14, Pin.OUT) #set Red LED to GP14
sck = Pin(6, Pin.OUT)    #set RFID sck to GP6
mosi = Pin(7, Pin.OUT)   #set RFID mosi to GP7
miso = Pin(4, Pin.OUT)   #set RFID miso to GP4 
sda = Pin(5, Pin.OUT)    #set RFID sda to GP5 
rst = Pin(18, Pin.OUT)   #set RFID rst to GP18
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso) #initial SPI 
card1 = "0xe58a6223" #change this value to match your testing RFID card 1
card2 = "0xf765bd60" #change this value to match your testing RFID card 2

while True:
    rdr = MFRC522(spi, sda, rst) #initialize reader
    (stat, tag_type) = rdr.request(rdr.REQIDL) #read card ud
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == card1: #if ID matches card 1, buzzer beep once, turn on Green LED
                print("card 1 detected!")
                buzzer.value(0)
                time.sleep(0.3)
                buzzer.value(1)
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
            elif uid == card2:
                print("card 2 detected!")  #if ID matches card 2, buzzer beep twice, turn on Green LED
                buzzer.value(0)
                time.sleep(0.3)
                buzzer.value(1)
                time.sleep(0.3)
                buzzer.value(0)
                time.sleep(0.3)
                buzzer.value(1)
                true.value(1)
                time.sleep(1)
                true.value(0)
                time.sleep(1)
            else:  #if ID doesn't match any card, long beep, turn on Red LED
                print("invalid card!")
                buzzer.value(0)
                time.sleep(2)
                buzzer.value(1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(0.1)
                false.value(1)
                time.sleep(0.1)
                false.value(0)
                time.sleep(1)