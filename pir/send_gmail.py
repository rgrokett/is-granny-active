#!/usr/bin/python
# Sends email daily 
# Run by crontab

import smtplib
import sys
import collections

# UPDATE GMAIL FIELDS BELOW WITH YOUR CREDENTIALS AND EMAIL IDs
SMTP_SERVER    = 'smtp.gmail.com:587'
GMAIL_USERNAME = 'YOUR_GMAIL_ID@gmail.com'
GMAIL_PASSWORD = 'YOUR_GMAIL_PASSWD' 

recipients     = ['YOUR_ID@gmail.com','FRIEND@yahoo.com','RELATIVE@att.net']
subject        = 'Grandma activity for today'
# 

cc_list = []

# SEND EMAIL
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems



#################
# MAIN
#################

# GET ACTIVITY FOR TODAY
hasharray = {} 

try:
  tot = 0;
  pos = 0;

  with open('daily.log') as f:
    for line in f:
	dayhour = line[0:20]
	if not dayhour in hasharray:
	    hasharray[dayhour] = 1
	else:
	    hasharray[dayhour] += 1
	tot += 1
except:
#  print "debug error:", sys.exc_info()[0]
  tot = 0;


if (tot > 0):
  emailText = "Activity was seen "+ str(tot) +" times today"
  emailText += "\n\n"
  emailText += "ACTIVITY  DAY/MO  HOUR   COUNT\n"
  hasharray = collections.OrderedDict(sorted(hasharray.items(), key=lambda t: t[0]))
  for (name,val) in hasharray.items():
	emailText += str(name) + ":00 = "+ str(val) + "\n"
else:
  emailText = 'NO ACTIVITY SEEN TODAY'

emailText = "" + emailText + ""

status = sendemail(GMAIL_USERNAME, recipients, cc_list, subject, emailText, GMAIL_USERNAME, GMAIL_PASSWORD, SMTP_SERVER)

print "STATUS:"+str(status)+"\n"


