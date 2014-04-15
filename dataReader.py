import time
import os
import RPi.GPIO as GPIO
from definitions import *
from random import *

def readChannel(adcnum, test=0):
        if test == 1:
            return randint(0,4095);
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(SPICS, True)

        GPIO.output(SPICLK, False)  # start clock low
        GPIO.output(SPICS, False)     # bring CS low

        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(SPIMOSI, True)
                else:
                        GPIO.output(SPIMOSI, False)
                commandout <<= 1
                GPIO.output(SPICLK, True)
                GPIO.output(SPICLK, False)

        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(14):
                GPIO.output(SPICLK, True)
                GPIO.output(SPICLK, False)
                adcout <<= 1
                if (GPIO.input(SPIMISO)):
                        adcout |= 0x1

        GPIO.output(SPICS, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout

def convertVolts(data):
 return data * 3.3/4095

def convertTemp(data):
 return (data-25)/12.4

def convertPressure(data):
 return data * 25/4095

def drive():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(SPICS, GPIO.OUT)
 GPIO.setup(SPIMISO, GPIO.IN)
 GPIO.setup(SPIMOSI, GPIO.OUT)
 GPIO.setup(SPICLK, GPIO.OUT)

 while True:
  a = 0
  for i in range(10):
    a += readChannel(0)
    time.sleep(0.01)
  a = a/10
  print a
