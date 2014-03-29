import threading
from definitions import *

def incrementMotor(servo, muscle, intensity, currentPosition, test=0):
  def threadIncrementMotor(servo, muscle, intensity, currentPosition, test=0):
    motor_id = 0
    if muscle == "CLAW":
      motor_id = CLAW_OUT
    elif muscle == "WRIST":
      motor_id = WRIST_OUT
    elif muscle == "ELBOW":
      motor_id = ELBOW_OUT
    increment = intensity * MUSCLE_FACTOR
    newPosition = currentPosition + increment
    if newPosition > SERVO_MAX:
      newPosition = SERVO_MAX
    elif newPosition < SERVO_MIN:
      newPosition = SERVO_MIN

    print "Rotating", muscle, "motor to position", newPosition
    if test == 0:
      servo.set_servo(motor_id, newPosition)
    currentPosition[0] = newPosition

    
  t = threading.Thread(target=threadIncrementMotor, args=(servo, muscle, intensity, currentPosition, test))
  t.start()
  t.join()
  return currentPosition
