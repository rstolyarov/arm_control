import spidev
import time
import os

def readChannel(channel):
  spi = spidev.SpiDev()
  spi.open(0,0)
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

def convertVolts(data,places):
  volts = (data * 3.3) / float(4095)
  volts = round(volts,places)
  return volts

def convertTemp(data,places):
  temp = round((data * 330)/float(4095),places)
  return temp

def convertPressure(data,places):
  pounds = (data * 25) / float(4095)

