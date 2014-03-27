import scipy.signal as sig
from defintions import *
import time
from readADC import *
from signalProcessing import *

def sampleUser(old_reads):

	claw1 = [0] * SAMPLE_NUMBER
	claw2 = [0] * SAMPLE_NUMBER
	wrist1 = [0] * SAMPLE_NUMBER
	wrist2 = [0] * SAMPLE_NUMBER
	elbow1 = [0] * SAMPLE_NUMBER
	elbow2 = [0] * SAMPLE_NUMBER

	emg_vectors = [claw1, claw2, wrist1, wrist2, elbow1, elbow2]
	for i in range(sample_number):
		for j in range(6):
			emg_vectors[j] = readadc(j, SPICLK, SPIMOSI, SPIMISO, SPICS)
		time.sleep(SAMPLE_PERIOD)

	new_reads = process_signal(emg_vectors)
  return new_reads

def sampleHeat():
  return 2.0

def sampleTouch():
  pass