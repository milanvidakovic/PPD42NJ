#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


# GPIO PORT for large particles
PORT_BIG = 20

# GPIO PORT for small particles
PORT_SMALL = 19	

GPIO.setmode(GPIO.BCM)
# GPIO PORT for large particles
GPIO.setup(PORT_BIG, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO PORT for small particles
GPIO.setup(PORT_SMALL, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
	measurement_count = 0
	smallPMCount = 0
	bigPMCount = 0
	for j in range(10*60):
		for i in range(1000):
			time.sleep(0.0001)
			input_value_big = GPIO.input(PORT_BIG)
			input_value_small = GPIO.input(PORT_SMALL)
			measurement_count += 1
			if input_value_small == 0:
				smallPMCount += 1
			if input_value_big == 0:
				bigPMCount += 1
		smallPMpercentRunning = 100.0 * smallPMCount / measurement_count
		bigPMpercentRunning = 100.0 * bigPMCount / measurement_count
	print smallPMpercentRunning
	print bigPMpercentRunning

