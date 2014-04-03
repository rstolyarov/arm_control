from RPIO import PWM
import RPi.GPIO as GPIO
from definitions import *
from pulseDegree import *
from indicatorLight import *
from inputSampling import *
from beeper import *
from incrementMotor import *
   

def control (servo):
  lightOn(LIGHT_OUT_BCM)
  print "running program"
  userInput = [0,0,0]
  heatInput = 0
  touchInput = 0
  clawPosition = [INIT_CLAW_POSITION]
  wristPosition = [INIT_WRIST_POSITION]
  elbowPosition = [INIT_ELBOW_POSITION]

  cont = ""
  while(cont != "n"):
    userInput = sampleUser(userInput,TEST)
    heatInput = sampleHeat(heatInput)
    touchInput = sampleTouch(touchInput)

    if (heatInput > HEAT_THRESH):
      print "too much heat!"
      beep(SOUND_OUT_BCM, 3)
    
    elbowPosition = incrementMotor(servo, "WRIST", userInput[0], elbowPosition, TEST)
    wristPosition = incrementMotor(servo, "ELBOW", userInput[1], wristPosition, TEST)
    
    if touchInput > TOUCH_THRESH and userInput[2] > 0:
      print "too much pressure!"
      beep(SOUND_OUT_BCM, 1)
    else:
      clawPosition = incrementMotor(servo, "CLAW", userInput[2], clawPosition)
    cont = raw_input("Shall we continue? (testing only) y/n:");
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
