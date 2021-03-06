import threading
from definitions import *
from RPIO import PWM
import time
import math

def incrementMotor(servo, muscle, intensity, currentPosition, test=0):
    motor_id = 0
    servo_max = None
    servo_min = None
    if muscle == "WRIST":
      motor_id = WRIST_OUT_BCM
      servo_max = SERVO_WRIST_MAX
      servo_min = SERVO_WRIST_MIN
    elif muscle == "ELBOW":
      motor_id = ELBOW_OUT_BCM
      servo_max = SERVO_ELBOW_MAX
      servo_min = SERVO_ELBOW_MIN
    increment = intensity * MUSCLE_FACTOR
    newPosition = currentPosition + increment

    if newPosition > servo_max:
      print "newPos > servomax",muscle
      newPosition = servo_max
    elif newPosition < servo_min:
      print "newPos < servomin",muscle
      newPosition = servo_min

    
    if test == 0 and intensity != 0 and currentPosition != newPosition:
       #servo.stop_servo(motor_id)
       servo.set_servo(motor_id, newPosition)
       print "Rotating",muscle,"to new position",newPosition
       currentPosition = newPosition
    return currentPosition

def initializeClawMotor(servo,test=0):
    if test == 1:
       print "Initializing claw"
       return
    motor_id = CLAW_OUT_BCM
    servo.set_servo(motor_id, CLAW_OPEN)
    time.sleep(1)
    servo.set_servo(motor_id, CLAW_CLOSE)
    time.sleep(CLAW_TIME_TO_NEUTRAL)
    servo.set_servo(motor_id, CLAW_NEUTRAL)

def incrementClawMotor(servo,intensity,test=0):
  def threadIncrementClawMotor(servo, intensity, test=0):
    if test == 1:
     print "Rotating claw with intensity",intensity
     return
    motor_id = CLAW_OUT_BCM
    if intensity>0:
      servo.set_servo(motor_id, CLAW_CLOSE)
      time.sleep(intensity*CLAW_DELAY_FACTOR)
    elif intensity<0:
      servo.set_servo(motor_id, CLAW_OPEN)
      time.sleep(intensity*-1*CLAW_DELAY_FACTOR)
    servo.set_servo(motor_id, CLAW_BRAKE)
  t = threading.Thread(target=threadIncrementClawMotor, args=(servo, intensity, test))
  t.start()
