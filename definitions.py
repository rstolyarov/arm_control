
#Motor position and range standards
SERVO_WRIST_MIN = 600
SERVO_WRIST_MAX = 2400
SERVO_WRIST_NEUTRAL = 1500
SERVO_CLAW_MIN = 600
SERVO_CLAW_MAX = 2400
SERVO_CLAW_NEUTRAL = 1500
SERVO_ELBOW_MIN = 1500
SERVO_ELBOW_MAX = 2400
SERVO_ELBOW_NEUTRAL = 1950 

CLAW_CLOSE = 1000
CLAW_OPEN = 2000
CLAW_BRAKE = 200
CLAW_NEUTRAL = 1500
CLAW_DELAY_FACTOR = 0.1
CLAW_TIME_TO_NEUTRAL = 0.1

INIT_CLAW_POSITION = SERVO_CLAW_NEUTRAL
INIT_WRIST_POSITION = SERVO_WRIST_NEUTRAL
INIT_ELBOW_POSITION = SERVO_ELBOW_NEUTRAL

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
HEAT_THRESH = 150 #Fahrenheit
TOUCH_THRESH = 15 #pounds

#Muscle indexing information
MUSCLE_FACTOR = 30 
MUSCLES = ["WRIST","ELBOW","CLAW"]

#Signal processing constants
SAMPLE_FREQUENCY = 2000 #Hz
SAMPLE_WINDOW = 0.03 #seconds
SAMPLE_NUMBER = SAMPLE_FREQUENCY * SAMPLE_WINDOW
SAMPLE_PERIOD = 1/SAMPLE_FREQUENCY 
OMEGA = 0.1
PI = 3.1415926
OMEGA_O = 2*PI*SAMPLE_WINDOW*SAMPLE_PERIOD
EMG_THRESH1 = 1000
EMG_THRESH2 = 2000
EMG_THRESH3 = 3000

#ADC channel input specifications
ANALOG_CLAW_IN = [0,1]
ANALOG_WRIST_IN = [2,3]
ANALOG_ELBOW_IN = [4,5]
ANALOG_TEMP_IN = 6
ANALOG_TOUCH_IN = 7

#Flags
TEST = 1
DEMO = 1

#Display info
HEADINGS = ["-- EMG Readings --", "EMG1: ", "EMG2: ", "EMG3: ", "EMG4 ", "EMG5: ", "EMG6: ", "-- Sensor Readings --", "Touch: ", "Heat: ", "-- Motor Positions --", "Claw: ", "Wrist: ", "Elbow: "]
VERTICALPOSITIONS = [10,25,40,55,70,85,100,130,145,160,190,205,220,235]
WARNINGS = ["Too much heat!", "Too much pressure!", "OKAY"]

