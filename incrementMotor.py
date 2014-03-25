import threading
from definitions import *
from positionFeedback import getCurrentPosition[i]

def incrementMotor(servo, i, intensity, factor):
  def threadIncrementMotor(servo, i, intensity,factor):
    motor_id = 0
    curPos = 0
  
    if i==0 or i==1: 
      motor_id = CLAW_OUT 
    if i==2 or i==3: 
      motor_id = WRIST_OUT
    if i==4 or i==5: 
      motor_id = ELBOW_OUT

    curPos = getCurrentPosition(i)

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
    
  t = threading.Thread(target=threadIncrementMotor, args=(servo,i,intensity,factor))
  t.start()