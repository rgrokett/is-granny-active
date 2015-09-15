# is-granny-active
Gathers daily motion detection activity and sends email

This python program is designed for Raspberry Pi with Ethernet or Wifi and a PIR motion sensor. Every motion event is logged to a file. Then once each morning, a cron runs another program that reads the log for the past 24 hrs and sends an email via your gmail account to any desired persons such as a friend or relative. By placing the Pi in an area of the house, such as a living room or kitchen, you can track activity without being intrusive (such as would occur with a webcam).  

STEPS:
<ol>
<li>Setup of the Raspberry Pi with PIR motion sensor
<li>Install & configure the granny-active software
<li>Test and Deploy
</ol>

FILES:
<pre>
morning.sh      -- Runs daily send mail & Resets daily log<br>
pir.py          -- PIR Montion Detector runs all the time<br>
run.sh          -- run from /etc/rc.local at bootup<br>
daily.log       -- timestamps for any daily motion activity<br>
send_gmail.py   -- Sends emails out<br>
</pre>

CRON:
<pre>
pi Cron<br>
00 08 * * * /home/pi/morning.sh >/home/pi/email.log 2>&1

</pre>
