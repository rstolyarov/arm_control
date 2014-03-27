OUTPINS = [3,5,7,8,10,12,22,26]
INPINS = [13,15,16,18]

CLAW_OUT = 3
WRIST_OUT = 5
ELBOW_OUT = 7
LIGHT_OUT = 8
SOUND_OUT = 10
SPICLK = 12
TOUCH_IN = 13
TEMPA_IN = 15
TEMPB_IN = 16
#CLAWA_IN = 15
#CLAWB_IN = 16
SPIMISO = 18
#WRISTA_IN = 19
#WRISTB_IN = 21
SPICS = 22
#ELBOWA_IN = 23
#ELBOWB_IN = 24
SPIMOSI = 26

INIT_CLAW_ANGLE = 45
INIT_WRIST_ANGLE = 45
INIT_ELBOW_ANGLE = 45 

HEAT_THRESH = 1.0
TOUCH_THRESH = 1.0
MUSCLE_FACTOR = 10.0 

SAMPLE_FREQUENCY = 2000 #Hz
SAMPLE_WINDOW = 0.03 #seconds
SAMPLE_NUMBER = SAMPLE_FREQUENCY * SAMPLE_WINDOW
SAMPLE_PERIOD = 1/SAMPLE_FREQUENCY 