def lightOn(LIGHT_OUT):
  print "light on"
  GPIO.output(LIGHT_OUT,True)

def lightOff(LIGHT_OUT):
  print "light off"
  GPIO.output(LIGHT_OUT,False)