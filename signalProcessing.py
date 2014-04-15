from definitions import *
from scipy.signal import *
import numpy
import math
import random

def processDirections(speeds, diff=False):
	speeds3 = [0]*3
	if diff:
	  for i in range(3):
	    speeds3[i] = speeds[2*i]-speeds[2*i+1]
	else:
	  for i in range(3):
	  	if speeds[2*i] > speeds[2*i+1]:
	  		speeds3[i] = speeds[2*i]
	  	elif speeds[2*i] < speeds[2*i+1]:
	  		speeds3 = -1 * speeds[2*i+1]
	  	else:
	  		print "Unable to tell if flexing or extending muscle",MUSCLES[i]
	return speeds3

def process(signal):
	#digital filter for motion artifact below 20 Hz
	N1=4   #filter order
	Wn1=20/(0.5*SAMPLE_FREQUENCY)
	[Bhp,Ahp]=butter(N1,Wn1,'highpass')  #creates digital filter
	signal1 = lfilter(Bhp,Ahp,signal) #filter function applies filter to signal

	#digital lowpass filter (at 300Hz - band-limiting)
	N2=4  #filter order
	Wn2=300/(0.5*SAMPLE_FREQUENCY)
	[Blp,Alp]=butter(N2,Wn2,'lowpass') 
	signal2 = lfilter(Blp,Alp,signal1)

	#digital notch filter for 60Hz noise
	k1 = -math.cos(OMEGA_O)
	k2 = (1 - math.tan(OMEGA/2))/(1+math.tan(OMEGA/2))
	B = [k2, k1*(1+k2), 1]
	A = [1, k1*(1+k2), k2]

	#notch filter is 0.5*(1+B/A)
	B1 = [0,0,0]
	for i in range(3):
		B1[i] = (B[i] + A[i])/2;
	signal3=lfilter(B1,A,signal2) 

	# Linear envelope post processing 
	# Fe=SAMPLE_FREQUENCY #Sampling frequency in Hz *found value in literature*
	# Fc=10; % Cut-off frequency 
	# N=4; % Filter Order
	# [B, A] = butter(N,Fc*2/Fe, 'low')
	# Processed_EMG=filter(B,A, signal3) 

	
	EMGamp = numpy.sqrt(numpy.mean(signal3**2)) #Root Mean Square
	speed = 0
	if EMGamp > EMG_THRESH1:
 		speed = 1
	elif EMGamp > EMG_THRESH2:
  		speed = 2
	elif EMGamp > EMG_THRESH3:
  		speed = 3

	return speed, EMGamp

def processSignal(emg_vectors, test=0):
    if test==0:
	  speeds6 = [0]*6
          rawRMS = [0]*6
	  for i in range(6):
		speeds6[i], rawRMS[i] = process(emg_vectors[i])
	  speeds3 = processDirections(speeds6)
	
	  return speeds3, rawRMS
    else:
      return [test]*3, [test]*6
