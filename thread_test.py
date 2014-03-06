import RPi.GPIO as GPIO
import time
import sys
from numpy import arange
import threading

def beep():
  def beeper(a):
    numTimes = 100
    speed = 0.001
    soundPort = int(sys.argv[1])
    numBeeps = int(sys.argv[2])
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(soundPort, GPIO.OUT)
    for i in range(numBeeps):
      for j in range(numTimes):
        GPIO.output(soundPort, True)
        time.sleep(speed)
        GPIO.output(soundPort, False)
        time.sleep(speed)
      time.sleep(0.1)
    GPIO.cleanup()
  t = threading.Thread(target=beeper,args=("5"))
  t.start()

def listnums():
  def lisn(a):
    for i in range(100000):
      print i
  u = threading.Thread(target=lisn,args=("1"))
  u.start()


beep()
listnums()
