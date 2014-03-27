import scipy.signal as sig
from RPIO import PWM
import RPi.GPIO as GPIO
from definitions import *
from pulseDegree import PulToDeg,DegToPul
from indicatorLight import lightOn,lightOff
from inputSampling import sampleUser, sampleHeat, sampleTouch
from beeper import beep
   

def control (servo):
  lightOn(LIGHT_OUT)
  print "running program"
  userInput = [0,0,0,0,0,0]
  heatInput = 0
  touchInput = 0
  while(True):
    userInput = sampleUser(userInput)
    heatInput = sampleHeat(heatInput)
    if (heatInput > HEAT_THRESH):
      print "too much heat!"
      beep(SOUND_OUT, 3)
    for i in range(0,5):
      intensity = userInput[i]
      incrementMotor(servo, i, intensity, MUSCLE_FACTOR)
    if userInput[5]:
      touchInput = sampleTouch(touchInput)
      if (touchInput > TOUCH_THRESH):
        print "too much pressure!"
        beep(SOUND_OUT, 3)
      else:
        incrementMotor(5, userInput[5])
  lightOff(LIGHT_OUT)

def initGPIO():
  GPIO.setmode(GPIO.BOARD)
  for outpin in outpins:
    print "setting up pin "+str(outpin)
    GPIO.setup(outpin, GPIO.OUT)
  for inpin in inpins:
    print "setting up pin "+str(inpin)
    GPIO.setup(inpin, GPIO.IN)
  servo = PWM.Servo()
  return servo  

servo = initGPIO()
control(servo)
