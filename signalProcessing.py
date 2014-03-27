from definitions import *
import numpy

def process(emg_vec):
	return mean(emg_vec)

def processSignal(emg_vectors):
	averages = [0]*6
	for i in range(6):
		averages[i] = process(emg_vectors[i])

	return averages

def processSignalTesting(emg_vectors):
	return [0,1,0,0,3,0]