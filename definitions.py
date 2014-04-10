
#Motor position and range standards
SERVO_MIN = 600
SERVO_MAX = 2400
SERVO_NEUTRAL = 1500
INIT_CLAW_POSITION = SERVO_NEUTRAL
INIT_WRIST_POSITION = SERVO_NEUTRAL
INIT_ELBOW_POSITION = SERVO_NEUTRAL

#GPIO pin specifications
OUTPINS_BCM = [7,8,10,11,14,15,18,23]
INPINS_BCM = [9]
LIGHT_OUT_BCM = 14
SOUND_OUT_BCM = 15
CLAW_OUT_BCM = 7
WRIST_OUT_BCM = 18
ELBOW_OUT_BCM = 23

#ADC pin specifications
SPICS = 8
SPIMISO = 9
SPIMOSI = 10
SPICLK = 11

#Sensory thresholds
HEAT_THRESH = 200
TOUCH_THRESH = 25

#Muscle indexing information
MUSCLE_FACTOR = 150 
MUSCLES = ["WRIST","ELBOW","CLAW"]

#Signal processing constants
SAMPLE_FREQUENCY = 2000 #Hz
SAMPLE_WINDOW = 0.03 #seconds
SAMPLE_NUMBER = SAMPLE_FREQUENCY * SAMPLE_WINDOW
SAMPLE_PERIOD = 1/SAMPLE_FREQUENCY 
OMEGA = 0.1
PI = 3.1415926
OMEGA_O = 2*PI*SAMPLE_WINDOW*SAMPLE_PERIOD #discrete-time notch frequency (in rad) (60Hz)
EMG_THRESH1 = 1000
EMG_THRESH2 = 2000
EMG_THRESH3 = 3000

#ADC channel input specifications
ANALOG_CLAW_IN = [0,1]
ANALOG_WRIST_IN = [2,3]
ANALOG_ELBOW_IN = [4,5]
ANALOG_TEMP_IN = 6
ANALOG_TOUCH_IN = 7

#Testing flag
TEST = 1

#Display info
HEADINGS = ["-- EMG Readings --", "EMG1: ", "EMG2: ", "EMG3: ", "EMG4 ", "EMG5: ", "EMG6: ", "-- Sensor Readings --", "Touch: ", "Heat: ", "-- Motor Positions --", "Claw: ", "Wrist: ", "Elbow: "]
VERTICALPOSITIONS = [10,25,40,55,70,85,100,130,145,160,190,205,220,235]
WARNINGS = ["Too much heat!", "Too much pressure!", "OKAY"]

