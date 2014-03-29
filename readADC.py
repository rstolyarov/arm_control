#!/usr/bin/env python
import time
import os
import RPi.GPIO as GPIO
from incrementMotor import incrMotor
from definitions import *
 
GPIO.setmode(GPIO.BCM)
DEBUG = 1
 
# read SPI data from MCP3008 chip, 8 possible adc's (0 thru 7)
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
        if ((adcnum > 7) or (adcnum < 0)):
                return -1
        GPIO.output(cspin, True)
 
        GPIO.output(clockpin, False)  # start clock low
        GPIO.output(cspin, False)     # bring CS low
 
        commandout = adcnum
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
                if (commandout & 0x80):
                        GPIO.output(mosipin, True)
                else:
                        GPIO.output(mosipin, False)
                commandout <<= 1
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):
                GPIO.output(clockpin, True)
                GPIO.output(clockpin, False)
                adcout <<= 1
                if (GPIO.input(misopin)):
                        adcout |= 0x1
 
        GPIO.output(cspin, True)
        
        adcout >>= 1       # first bit is 'null' so drop it
        return adcout


def sampleForEMG(servo, last_reads):

    # 10k trim pot connected to adc #0
    tolerance = 5       # to keep from being jittery we'll only change
                    # volume when the pot has moved more than 5 'counts'
    sig_adjusts = [0,0,0,0,0,0]
         # we'll assume that the pot didn't move
    sigs_changed = [False,False,False,False,False,False]
 
    # read the analog pin
    new_reads = [0,0,0,0,0,0]
    for i in range(6):
        new_reads[i] = readadc(i, SPICLK, SPIMOSI, SPIMISO, SPICS)
        # how much has it changed since the last read?
        motor_adjusts[i] = abs(new_reads[i] - last_reads[i])
 
        if DEBUG:
            print "new_motor_read:", i, new_reads[i]
            print "sig_adjust:", i, sig_adjusts[i]
            print "last_motor_read:", i, last_reads[i]
 
        if ( sig_adjusts[i] > tolerance ):
           sigs_changed[i] = True
 
        if DEBUG:
            print "sig_changed", i, sig_changed[i]
 
        if ( sig_changed[i]):
            # set_volume = trim_pots[i] / 10.24           # convert 10bit adc0 (0-1024) trim pot read into 0-100 volume level
            # set_volume = round(set_volume)          # round out decimal value
            # set_volume = int(set_volume)            # cast volume as integer
 
            # print 'Volume = {volume}%' .format(volume = set_volume)
            intensity = processSignal(sig_adjusts[i])
            incrMotor(servo, i, intensity, MUSCLE_FACTOR)
 
            if DEBUG:
                print "set_volume", set_volume
                print "tri_pot_changed", set_volume
 
                # save the potentiometer reading for the next loop
                last_reads[i] = new_reads[i]
 
    # hang out and do nothing for a half second
    time.sleep(0.5)