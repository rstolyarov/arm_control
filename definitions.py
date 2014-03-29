
SERVO_MIN = 600
SERVO_MAX = 2400
SERVO_NEUTRAL = 1500

OUTPINS = [3,5,7,8,10,12,22,26]
INPINS = [13,15,16,18]

CLAW_OUT = 3
WRIST_OUT = 5
ELBOW_OUT = 7
LIGHT_OUT = 8
SOUND_OUT = 10
SPICLK = 12
SPIMISO = 18
SPICS = 22
SPIMOSI = 26

INIT_CLAW_POSITION = SERVO_NEUTRAL
INIT_WRIST_POSITION = SERVO_NEUTRAL
INIT_ELBOW_POSITION = SERVO_NEUTRAL

HEAT_THRESH = 60
TOUCH_THRESH = 25
MUSCLE_FACTOR = 150 

SAMPLE_FREQUENCY = 2000 #Hz
SAMPLE_WINDOW = 0.03 #seconds
SAMPLE_NUMBER = SAMPLE_FREQUENCY * SAMPLE_WINDOW
SAMPLE_PERIOD = 1/SAMPLE_FREQUENCY 

ANALOG_CLAW_IN = [0,1]
ANALOG_WRIST_IN = [2,3]
ANALOG_ELBOW_IN = [4,5]
ANALOG_TEMP_IN = 6
ANALOG_TOUCH_IN = 7

ROUND = 2

TEST = 1