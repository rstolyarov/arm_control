import threading
from definitions import *
from positionFeedback import getCurrentPosition[i]

def incrementMotor(servo, muscle, intensity, currentPosition, test=0):
  def threadIncrementMotor(servo, muscle, intensity, currentPosition, test=0):
    motor_id = 0
    if muscle == "CLAW":
      motor_id = CLAW_OUT
    else if muscle == "WRIST":
      motor_id = WRIST_OUT
    else if muscle == "ELBOW":
      motor_id = ELBOW_OUT
    increment = intensity * MUSCLE_FACTOR
    newPosition = currentPosition + increment
    print "Rotating", muscle, "motor to position", newPosition
    if test == 0:
      servo.set_servo(motor_id, newPosition)
    return newPosition

    
  t = threading.Thread(target=threadIncrMotor, args=(servo, muscle, intensity, currentPosition, test))
  t.start()