#!/bin/bash
# RESTART PIR Motion Sensor
cd /home/pi
sudo mv daily.log daily.log.bak
sudo rm nohup.out
sudo nohup python -u ./pir.py &

