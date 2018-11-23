#!/bin/bash
# RESTART PIR Motion Sensor
cd /home/pi
sudo mv daily.log daily.log.bak
sudo python -u ./send_ifttt.py RESTART > /home/pi/email.log 2>&1
sudo rm nohup.out
sudo nohup python -u ./pir.py &

