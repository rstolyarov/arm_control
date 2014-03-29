from RPIO import PWM
import RPi.GPIO as GPIO
from definitions import *
from pulseDegree import *
from indicatorLight import *
from inputSampling import *
from beeper import *
from incrementMotor import *
   

def control (servo):
  lightOn(LIGHT_OUT)
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
    heatInput = sampleHeat(heatInput,TEST)
    touchInput = sampleTouch(touchInput, TEST)

    if (heatInput > HEAT_THRESH):
      print "too much heat!"
      beep(SOUND_OUT, 3)
    
    elbowPosition = incrementMotor(servo, "ELBOW", userInput[0], elbowPosition, TEST)
    wristPosition = incrementMotor(servo, "WRIST", userInput[1], wristPosition, TEST)
    
    if touchInput > TOUCH_THRESH and userInput[2] > 0:
      print "too much pressure!"
      beep(SOUND_OUT, 1)
    else:
      clawPosition = incrementMotor(servo, "CLAW", userInput[2], clawPosition, TEST)
    cont = raw_input("Shall we continue? (testing only) y/n:");
  lightOff(LIGHT_OUT)

def initServoPositions(servo, test):
  print "Initialized servo positions"
  if test == 0:
    servo.set_servo(CLAW_OUT, INIT_CLAW_POSITION)
    servo.set_servo(WRIST_OUT, INIT_WRIST_POSITION)
    servo.set_servo(ELBOW_OUT, INIT_ELBOW_POSITION)

def initGPIO():
  GPIO.setmode(GPIO.BOARD)
  for outpin in OUTPINS:
    print "setting up pin "+str(outpin)
    GPIO.setup(outpin, GPIO.OUT)
    GPIO.output(outpin, False)
  for inpin in INPINS:
    print "setting up pin "+str(inpin)
    GPIO.setup(inpin, GPIO.IN)
  servo = PWM.Servo()
  return servo  

servo = initGPIO()
initServoPositions(servo, TEST)
control(servo)
