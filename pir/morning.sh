#!/bin/bash
# Add this to "pi" CRONTAB
#00 08 * * * /home/pi/morning.sh

cd /home/pi

# send activity for past 24 hrs
# Send via IFTTT
sudo python -u ./send_ifttt.py

# reset log
sudo mv daily.log daily.log.bak

