import scipy.signal as sig
from definitions import *
import time
from signalProcessing import *
from dataReader import *

def sampleUser(old_reads, test=0, supertest=0):
  if test == 0:
	  claw1 = [0] * SAMPLE_NUMBER
	  claw2 = [0] * SAMPLE_NUMBER
	  wrist1 = [0] * SAMPLE_NUMBER
	  wrist2 = [0] * SAMPLE_NUMBER
	  elbow1 = [0] * SAMPLE_NUMBER
	  elbow2 = [0] * SAMPLE_NUMBER

	  emg_vectors = [wrist1, wrist2, elbow1, elbow2, claw1, claw2]
	  for i in range(SAMPLE_NUMBER):
	    for j in range(6):
		    emg_vectors[i] = readChannel(i);
	    time.sleep(SAMPLE_PERIOD)
          new_reads = processSignal(emg_vectors, supertest)
	  print "User sampled (WRIST,ELBOW,CLAW):",new_reads
          return new_reads
  else:
    a = int(raw_input("Enter wrist intensity."));
    b = int(raw_input("Enter elbow intensity."));
    c = int(raw_input("Enter claw intensity."));
    new_reads = [a,b,c]
    print "User sampled:",new_reads
    return new_reads

def sampleHeat(old_read, test=0):
  if test == 0:
	raw_data = readChannel(ANALOG_TEMP_IN)
	new_read = convertTemp(raw_data)
        print "Heat sampled:",new_read,"(raw data=",raw_data
  	return new_read
  else:
  	new_read = int(raw_input("Enter heat input."));
  	print "Heat sampled:",new_read
        return new_read

def sampleTouch(old_read, test=0):
  if test == 0:
	raw_data = readChannel(ANALOG_TOUCH_IN)
	new_read = convertPressure(raw_data)
        print "Touch sampled:",new_read,"(raw data=",raw_data
	return new_read
  else:
  	new_read = int(raw_input("Enter touch input."));
  	print "Touch sampled:",new_read
  	return new_read




