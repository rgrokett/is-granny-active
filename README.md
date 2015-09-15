# is-granny-active
Gathers daily motion detection activity and sends email

This python program is designed for Raspberry Pi with Ethernet or Wifi and a PIR motion sensor. Every motion event is logged to a file. Then once each morning, a cron runs another program that reads the log for the past 24 hrs and sends an email via your gmail account to any desired persons such as friend or relative. By placing the Pi in an area of the house, such as living room or kitchen, you can track activity without being intrusive (such as would occur with a webcam).  

STEPS:

1) Setup of the Raspberry Pi with PIR motion sensor

2) Install & configure the granny-active software

3) Test and Deploy

