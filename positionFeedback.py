
def getCurrentPosition(i):
  if i==0 or i==1: 
    return clawPos 
  if i==2 or i==3: 
    return wristPos
  if i==4 or i==5: 
    return elbowPos

def setCurrentPosition(i, angle):
  if i==0 or i==1: 
    clawPos = angle 
  if i==2 or i==3: 
    wristPos = angle
  if i==4 or i==5: 
    elbowPos = angle
