import threading
import time


#Beeps [numBeeps] times, each beep length 0.1 seconds and separated by 0.2 seconds
def beep(SOUND_OUT, numBeeps):
  def threadBeep(SOUND_OUT, numBeeps):
    print "Begin beeping"
    duration = 100
    speed = 0.001
    for i in range(int(numBeeps)):
      for j in range(duration):
        GPIO.output(SOUND_OUT,True)
        time.sleep(speed)
        GPIO.output(SOUND_OUT,False)
        time.sleep(speed)
      time.sleep(0.1)
  t = threading.Thread(target=threadBeep,args=(str(SOUND_OUT), str(numBeeps)))
  t.start()