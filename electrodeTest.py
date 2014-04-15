from definitions import *
import time
from signalProcessing import *
import matplotlib.pyplot as plt
from dataReader import *

claw1 = [0] * SAMPLE_NUMBER
claw2 = [0] * SAMPLE_NUMBER
wrist1 = [0] * SAMPLE_NUMBER
wrist2 = [0] * SAMPLE_NUMBER
elbow1 = [0] * SAMPLE_NUMBER
elbow2 = [0] * SAMPLE_NUMBER
times = [0.0] * SAMPLE_NUMBER
emg_vector_names = ["wrist1", "wrist2", "elbow1", "elbow2", "claw1", "claw2"]
emg_vectors = [wrist1, wrist2, elbow1, elbow2, claw1, claw2]

for i in range(SAMPLE_NUMBER):
  for j in range(6):
	emg_vectors[j][i] = readChannel(j, TEST);
  times[i] = SAMPLE_PERIOD*i;
  time.sleep(SAMPLE_PERIOD)


for k in range(6):
	speed, RMS = process(emg_vectors[k])
	print emg_vector_names[k], "RMS for 30ms window (",SAMPLE_NUMBER," samples):",RMS

p1, = plt.plot(times, claw1, 'r')
p2, = plt.plot(times,wrist1,'b')
p3, = plt.plot(times,elbow1,'g')
plt.legend([p3, p2, p1], ["elbow1","wrist1","claw1"])
plt.show()
  
