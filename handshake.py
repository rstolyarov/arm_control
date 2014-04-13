from RPIO import PWM
import RPi.GPIO as GPIO
from definitions import *
import time

servo = PWM.Servo()
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLAW_OUT_BCM, GPIO.OUT)
GPIO.setup(WRIST_OUT_BCM, GPIO.OUT)
for i in range(10):
  time.sleep(0.2)
  servo.set_servo(CLAW_OUT_BCM, 2000)
  servo.set_servo(WRIST_OUT_BCM, 1500)
  time.sleep(0.2)
  servo.set_servo(CLAW_OUT_BCM, 1000)
  servo.set_servo(WRIST_OUT_BCM, 1200)
  
