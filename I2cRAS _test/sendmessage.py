# -*- coding: utf-8 -*-
import smbus
import time

bus = smbus.SMBus(1)

address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
    var = int(input('Enter 1 – 9: '))
    writeNumber(var)
    print ('RPI: Hi Arduino, I sent you ', var)
    time.sleep(1)
    number = readNumber()
    print ('Arduino: Hey RPI, I received a digit ', number)
    if(var==number):
        print('message send successfully')
        break
    
