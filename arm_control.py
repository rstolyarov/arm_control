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

def demo (servo, canvas, sigs, motors, warning, wristPosition, elbowPosition, i, move):
  if i % 10 == 0:
      move = [randint(-3,3),randint(-3,3),randint(-3,3)]
  i=i+1
  wristPosition = incrementMotor(servo, "WRIST", move[0], wristPosition)
  elbowPosition = incrementMotor(servo, "ELBOW", move[1], elbowPosition)
  heatInput = sampleHeat()
  touchInput = sampleTouch()
  incrementClawMotor(servo, move[2])
  clawPosition = "NEUTRAL"
  if move[2] > 0:
    clawPosition = "CLOSE",move[2]
  elif move[2] < 0:
    clawPosition = "OPEN",move[2]*-1
  values = ["DEMO","DEMO","DEMO","DEMO","DEMO","DEMO",touchInput,int(heatInput),wristPosition,elbowPosition,clawPosition]
  sigs, motors = renderNewValues(canvas, values, sigs, motors)
  canvas.after(1,demo,servo, canvas,sigs,motors,warning, wristPosition, elbowPosition, i, move)

def control (servo,canvas, sigs, motors, warning, wristPosition, elbowPosition, i):
  userInput = [0,0,0]
  i = i + 1
  heatInput = 0
  touchInput = 0 
  supertest = 1
  if i % 500 == 0:
      cycleCount = 0
      supertest = -1 * supertest
  userInput, rawRMS = sampleUser()
  heatInput = sampleHeat()
  touchInput = sampleTouch()

  if 0 in rawRMS:
    warning = renderWarning(canvas, 2, warning)
  else:
    warning = renderWarning(canvas, 3, warning)
  if (heatInput > HEAT_THRESH):
      warning = renderWarning(canvas, 0, warning)
      beep(SOUND_OUT_BCM, 3)
    
  wristPosition = incrementMotor(servo, "WRIST", userInput[0], wristPosition)
  elbowPosition = incrementMotor(servo, "ELBOW", userInput[1], elbowPosition)
  clawPosition = "Neutral"
  if touchInput > TOUCH_THRESH and userInput[2] > 0:
      warning = renderWarning(canvas, 1, warning)
      servo.set_servo(CLAW_OUT_BCM, CLAW_BRAKE)
      clawPosition = "BRAKE"
      beep(SOUND_OUT_BCM, 1)
  else:
      incrementClawMotor(servo, userInput[2])
      if userInput[2] > 0:
        clawPosition = "CLOSE",userInput[2]
      elif userInput[2] < 0:
        clawPosition = "OPEN",userInput[2] 
  #cont = raw_input("Shall we continue? (testing only) y/n:");
  values=[rawRMS[0], rawRMS[1], rawRMS[2], rawRMS[3], rawRMS[4], rawRMS[5], touchInput, int(heatInput), wristPosition, elbowPosition, clawPosition]
  sigs, motors = renderNewValues(canvas, values, sigs, motors)
  canvas.after(1,control,servo,canvas,sigs,motors,warning, wristPosition,elbowPosition,i)

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


def main(canvas, sigs, motors, warning):

  servo = initGPIO()
  initServoPositions(servo)
  time.sleep(3)
  wristPosition = INIT_WRIST_POSITION
  elbowPosition = INIT_ELBOW_POSITION
  lightOn(LIGHT_OUT_BCM)
  i = 0
  move = [3,3,3]
  lightOn(LIGHT_OUT_BCM)
  if int(sys.argv[1]) == 1:	
    print "running demo (no interfacing with user)"
    canvas.after(1,demo, servo, canvas, sigs, motors, warning, wristPosition, elbowPosition, i, move)
  else:
    print "running full program (includes user interfacing)"
    canvas.after(1,control,servo,canvas,sigs,motors, warning, wristPosition,elbowPosition, i)

def renderNewValues(canvas,values, sigs,motors):
	
	for i in sigs:
		if i != None:
			canvas.delete(i)
	for j in motors:
		if j != None:
			canvas.delete(j)
	for i in range(6):
		sigs[i] = canvas.create_text(LEFT_MARGIN, VERTICAL_POSITIONS[i+1], text=values[i])
	for i in range(6,8):
		sigs[i] = canvas.create_text(LEFT_MARGIN, VERTICAL_POSITIONS[i+2], text=values[i])
	for i in range(3):
		motors[i] = canvas.create_text(LEFT_MARGIN, VERTICAL_POSITIONS[i+11], text=values[i+8])

	return sigs, motors

def renderWarning(canvas, value, warning):
	canvas.delete(warning)
	color = None
	if value == 3:
		color = "blue"
	else:
		color = "red"
	warning = canvas.create_text(WARNING_POSITION_H, WARNING_POSITION_V, fill=color,font=("Purisa",16),text=WARNINGS[value])
	return warning

def renderHeadings(canvas):
        canvas.create_text(TITLE_POSITION_H, TITLE_POSITION_V, font=("Purisa",20), text="Artificial Arm")
	for i in range(14):
		canvas.create_text(100,VERTICAL_POSITIONS[i],text=HEADINGS[i])
	return canvas

root = Tk()
canvas = Canvas(root, width=GUI_WIDTH, height=GUI_HEIGHT)
canvas.pack()

sigs = [None]*8
motors = [None]*3
warning = None

print "rendering headings"
canvas = renderHeadings(canvas)
warning = renderWarning(canvas,3,warning)
canvas.after(1,main, canvas, sigs, motors, warning)
root.mainloop()