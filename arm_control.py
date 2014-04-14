from RPIO import PWM
import RPi.GPIO as GPIO
from definitions import *
from pulseDegree import *
from indicatorLight import *
from inputSampling import *
from beeper import *
from incrementMotorP import *
from random import randint
from Tkinter import *
import sys

def demo (servo, canvas, sigs, motors, wristPosition, elbowPosition, i, move):
  lightOn(LIGHT_OUT_BCM)
  print "running demo (no interfacing with user)"
  print i
  if i % 100 == 0:
      print "CHANGED MOVE"
      move = [randint(-3,3),randint(-3,3),randint(-3,3)]
  i=i+1
  print "move:",repr(move)
  wristPosition = incrementMotor(servo, "WRIST", move[0], wristPosition)
  elbowPosition = incrementMotor(servo, "ELBOW", move[1], elbowPosition)
  incrementClawMotor(servo, move[2])
  values = [1,1,1,1,1,1,1,1,wristPosition,elbowPosition,1]
  sigs, motors = renderNewValues(canvas, values, sigs, motors)
  canvas.after(1,demo,servo, canvas,sigs,motors,wristPosition, elbowPosition, i, move)

def control (servo,canvas, sigs, motors, wristPosition, elbowPosition, i, demo=0):
      
  lightOn(LIGHT_OUT_BCM)
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


def main(canvas, sigs, motors):
  values = [0]*11
  sigs,motors = renderNewValues(canvas, values, sigs, motors)
  servo = initGPIO()
  initServoPositions(servo)
  time.sleep(3)
  wristPosition = INIT_WRIST_POSITION
  elbowPosition = INIT_ELBOW_POSITION
  lightOn(LIGHT_OUT_BCM)
  i = 0
  move = [3,3,3]
  if int(sys.argv[1]) == 1:	
    canvas.after(1,demo, servo, canvas, sigs, motors, wristPosition, elbowPosition, i, move)
  else:
    canvas.after(1,control,servo,canvas,sigs,motors,wristPosition,elbowPosition, i)

def renderNewValues(canvas,values, sigs,motors):
	k = 130
	for i in sigs:
		if i != None:
			canvas.delete(i)
	for j in motors:
		if j != None:
			canvas.delete(j)
	for i in range(6):
		sigs[i] = canvas.create_text(k, VERTICAL_POSITIONS[i+1], text=values[i])
	for i in range(6,8):
		sigs[i] = canvas.create_text(k, VERTICAL_POSITIONS[i+2], text=values[i])
	for i in range(3):
		motors[i] = canvas.create_text(k, VERTICAL_POSITIONS[i+11], text=values[i+8])

	return sigs, motors

def renderHeadings(canvas):
	for i in range(14):
		canvas.create_text(100,VERTICAL_POSITIONS[i],text=HEADINGS[i])
	return canvas

root = Tk()
canvas = Canvas(root, width=300, height=500)
canvas.pack()

sigs = [None]*8
motors = [None]*3

print "rendering headings"
canvas = renderHeadings(canvas)
canvas.after(1,main, canvas, sigs, motors)
root.mainloop()