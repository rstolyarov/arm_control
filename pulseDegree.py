def PulToDeg(pulse):
  deg = 0.1*pulse-150
  return deg

def DegToPul(deg):
  pulse = 10*deg+1500
  return pulse