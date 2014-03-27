from definitions import *
import numpy

def process(emg_vec):
	return mean(emg_vec)

def process_signal(emg_vectors):
	averages = [0]*6
	for i in range(6):
		averages[i] = process(emg_vectors[i])

	return averages