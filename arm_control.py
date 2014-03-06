from RPIO import PWM
import RPi.GPIO as GPIO
from numpy import arange
import time
import os
import threading

def PulToDeg(pulse):
  deg = 0.1*pulse-150
  return deg

def DegToPul(deg):
  pulse = 10*deg+1500
  return pulse

def sampleUser():
  return [1,0,1,0,1,0]

def sampleHeat():
  return 2.0

def sampleTouch():
  pass

def incrementMotor(servo, i, intensity, factor):
  motor_id = 0
  curPos = 0
  
  if i==0 or i==1: 
    motor_id = CLAW_OUT 
    curPos = clawPos
  if i==2 or i==3: 
    motor_id = WRIST_OUT
    curPos = wristPos
  if i==4 or i==5: 
    motor_id = ELBOW_OUT
    curPos = elbowPos
  
  increment = intensity * factor
  newPos = 0
  
  if (i%2==0): 
    newPos = curPos + increment
  else: 
    newPos = curPos - increment
  servo.set_servo(motor_id, newPos)
  
  if i==0 or i==1: clawPos = newPos 
  if i==2 or i==3: wristPos = newPos 
  if i==4 or i==5: elbowPos = newPos

def lightOn():
  print "light on"
  GPIO.output(LIGHT_OUT,True)
  pass

def lightOff():
  print "light off"
  GPIO.output(LIGHT_OUT,False)
  pass

#Beeps [numBeeps] times, each beep length 0.1 seconds and separated by 0.2 seconds
def beep(numBeeps):
  def threadBeep(numBeeps):
    print "Begin beeping"
    duration = 100
    speed = 0.001
    for i in range(int(numBeeps)):
      for j in range(duration):
        GPIO.output(SOUND_OUT,True)
        time.sleep(speed)
        GPIO.output(SOUND_OUT,False)
        time.sleep(speed)
      time.sleep(0.1)
  t = threading.Thread(target=threadBeep,args=(str(numBeeps)))
  t.start()
   

def run (servo, heatThresh, touchThresh, muscleFactor):
  lightOn()
  print "running program"
  while(True):
    userInput = sampleUser()
    heatInput = sampleHeat()
    if (heatInput > heatThresh):
      print "too much heat!"
      beep(3)
    for i in range(0,5):
      intensity = userInput[i]
      incrementMotor(servo, i, intensity, muscleFactor)
    if userInput[5]:
      touchInput = sampleTouch()
      if (touchInput > touchThresh):
        print "too much pressure!"
        incrementMotor(5, userInput[5])
      else:
        beep(3)
  lightOff()

def main(servo):
  heatThresh = 1.0
  touchThresh = 1.0
  muscleFactor = 10.0
  soundFrequency = 1000
  run(servo, heatThresh, touchThresh, muscleFactor)


GPIO.setmode(GPIO.BOARD)

outpins = [3,5,7,8,10]
inpins = [11,12,13,15,16,18,19,21,22]

CLAW_OUT = 3
WRIST_OUT = 5
ELBOW_OUT = 7
LIGHT_OUT = 8
SOUND_OUT = 10
TEMPA_IN = 11
TEMPB_IN = 12
TOUCH_IN = 13
CLAWA_IN = 15
CLAWB_IN = 16
ELBOWA_IN = 18
ELBOWB_IN = 19
WRISTA_IN = 21
WRISTB_IN = 22

clawPos = 45
wristPos = 45
elbowPos = 45 

for outpin in outpins:
  print "setting up pin "+str(outpin)
  GPIO.setup(outpin, GPIO.OUT)
for inpin in inpins:
  print "setting up pin "+str(inpin)
  GPIO.setup(inpin, GPIO.IN)



servo = PWM.Servo()  
main(servo)
