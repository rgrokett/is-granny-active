#!/usr/bin/env python
# PIR Motion Detection
# Simple program to detect and log motion events

import RPi.GPIO as GPIO
import time

# Install the sensor on GPIO Pin 4
sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))

    if new_state == "HIGH":
      datetime = time.strftime('%d/%m %X')
      fh = open("daily.log", "a")
      fh.write("activity at:" + datetime + "\n")
      fh.close


