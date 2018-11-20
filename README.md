# is-granny-active
Gathers daily motion detection activity and sends email

This python program is designed for Raspberry Pi with Ethernet or Wifi and a PIR motion sensor. Every motion event is logged to a file. Then once each morning, a cron runs another program that reads the log for the past 24 hrs and sends an email via your gmail account to any desired persons such as a friend or relative. By placing the Pi in an area of the house, such as a living room or kitchen, you can track activity without being intrusive (such as would occur with a webcam).  

STEPS:
<ol>
<li>Setup of the Raspberry Pi with PIR motion sensor on GPIO pin 4 as in pir.py
<li>Set up a Webhook-to-SMS in IFTTT (if used)
<li>Copy all the files in pir folder to /home/pi<br>
<li>Configure the send_gmail.py and/or send_ifttt.py programs
<li>Edit morning.sh to run send_gmail.py or send_ifttt.py or both
<li>Test using $ python send_gmail.py or $ python send_ifttt.py
<li>Deploy into cron:  $ crontab cronfile
</ol>

FILES:
<pre>
morning.sh      -- Runs daily send mail & Resets daily log<br>
pir.py          -- PIR Montion Detector runs all the time<br>
run.sh          -- run from /etc/rc.local at bootup<br>
daily.log       -- timestamps for any daily motion activity<br>
send_gmail.py   -- Sends emails out<br>
send_ifttt.py   -- Sends SMS out<br>
</pre>

CRON:
<pre>
pi Cron<br>
00 08 * * * /home/pi/morning.sh >/home/pi/email.log 2>&1
</pre>

/etc/rc.local:
<pre>

/home/pi/run.sh >/dev/null 2>&1
exit 0
</pre>
