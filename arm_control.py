from RPIO import PWM
import RPi.GPIO as GPIO
from definitions import *
from pulseDegree import *
from indicatorLight import *
from inputSampling import *
from beeper import *
from incrementMotorP import *
from random import randint
import sys
#import arm_display

def control (servo, demo=0):
      
  lightOn(LIGHT_OUT_BCM)
  wristPosition = INIT_WRIST_POSITION
  elbowPosition = INIT_ELBOW_POSITION
  if demo == 1:
    print "running demo (no interfacing with user)"
    count = 0
    move=[3,3,3]
    while count < 5000:
      count = count+1
      print count
      if count % 100 == 0:
        move = [randint(-3,3),randint(-3,3),randint(-3,3)]
      print "move:",repr(move)
      wristPosition = incrementMotor(servo, "WRIST", move[0], wristPosition)
      elbowPosition = incrementMotor(servo, "ELBOW", move[1], elbowPosition)
      incrementClawMotor(servo, move[2])
    return
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
    
    wristPosition = incrementMotor(servo, "WRIST", userInput[0], wristPosition)
    elbowPosition = incrementMotor(servo, "ELBOW", userInput[1], elbowPosition)
    
    if touchInput > TOUCH_THRESH and userInput[2] > 0:
      print "too much pressure!"
      servo.set_servo(CLAW_OUT_BCM, CLAW_BRAKE)
      beep(SOUND_OUT_BCM, 1)
    else:
      incrementClawMotor(servo, userInput[2])
    cycleCount=cycleCount+1
    #cont = raw_input("Shall we continue? (testing only) y/n:");
  lightOff(LIGHT_OUT_BCM)
  GPIO.cleanup()

def initServoPositions(servo, test=0):
  print "Initializing servo positions"
  if test == 0:
    servo.set_servo(ELBOW_OUT_BCM, INIT_ELBOW_POSITION)
    servo.set_servo(WRIST_OUT_BCM, INIT_WRIST_POSITION)
    initializeClawMotor(servo)

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
time.sleep(5)
control(servo, int(sys.argv[1]))
