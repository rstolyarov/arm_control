def lightOn(LIGHT_OUT, test=0):
  print "light on"
  if test == 0:
    GPIO.output(LIGHT_OUT,True)

def lightOff(LIGHT_OUT, test=0):
  print "light off"
  if test == 0:
    GPIO.output(LIGHT_OUT,False)