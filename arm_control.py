from RPIO import PWM
import RPi.GPIO as GPIO
from definitions import *
from pulseDegree import *
from indicatorLight import *
from inputSampling import *
from beeper import *
from incrementMotor import *
from random import randint

def control (servo, demo=0):
      
  lightOn(LIGHT_OUT_BCM)
  clawPosition = [INIT_CLAW_POSITION]
  wristPosition = [INIT_WRIST_POSITION]
  elbowPosition = [INIT_ELBOW_POSITION]
  if demo == 1:
    print "running demo (no interfacing with user)"
    count = 0
    move=[1,1,1]
    while True:
      count = count+1
      if count % 1000 == 0:
        count = 0
        move = [randint(-3,3),randint(-3,3),randint(-3,3)]
      elbowPosition = incrementMotor(servo, "WRIST", move[0], elbowPosition)
      wristPosition = incrementMotor(servo, "ELBOW", move[1], wristPosition)
      clawPosition = incrementMotor(servo, "CLAW", move[2], clawPosition)
  print "running full program (includes user interfacing)"
  userInput = [0,0,0]
  heatInput = 0
  touchInput = 0 
  cycleCount = 0
  supertest = 1
  cont = ""
  while(cont != "n"):
    if cycleCount % 500 == 0:
      cycleCount = 0
      supertest = -1 * supertest
    userInput = sampleUser(userInput,TEST,supertest)
    heatInput = sampleHeat(heatInput)
    touchInput = sampleTouch(touchInput)

    if (heatInput > HEAT_THRESH):
      print "too much heat!"
      beep(SOUND_OUT_BCM, 3)
    
    elbowPosition = incrementMotor(servo, "WRIST", userInput[0], elbowPosition)
    wristPosition = incrementMotor(servo, "ELBOW", userInput[1], wristPosition)
    
    if touchInput > TOUCH_THRESH and userInput[2] > 0:
      print "too much pressure!"
      beep(SOUND_OUT_BCM, 1)
    else:
      clawPosition = incrementMotor(servo, "CLAW", userInput[2], clawPosition)
    cycleCount=cycleCount+1
    #cont = raw_input("Shall we continue? (testing only) y/n:");
  lightOff(LIGHT_OUT_BCM)
  GPIO.cleanup()

def initServoPositions(servo, test=0):
  print "Initializing servo positions"
  if test == 0:
    servo.set_servo(CLAW_OUT_BCM, INIT_CLAW_POSITION)
    servo.set_servo(WRIST_OUT_BCM, INIT_WRIST_POSITION)
    servo.set_servo(ELBOW_OUT_BCM, INIT_ELBOW_POSITION)

def initGPIO():
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)
  for outpin in OUTPINS_BCM:
    print "setting up pin "+str(outpin)
    GPIO.setup(outpin, GPIO.OUT)
  for inpin in INPINS_BCM:
    print "setting up pin "+str(inpin)
    GPIO.setup(inpin, GPIO.IN)
  servo = PWM.Servo()
  return servo  

servo = initGPIO()
initServoPositions(servo)
control(servo)
