#!/usr/bin/python
# Sends email daily 
# Run by crontab

import sys
import collections
import requests 


# IFTTT ACCOUNT INFO
api_key  = "{YOUR_IFTTT_API_KEY}" // Your API KEY from https://ifttt.com/maker
event    = "morning_message"
host     = "maker.ifttt.com"


# SEND IFTTT
def sendifttt(message):
    DATA = { 'value1' : message }
    URL = "https://maker.ifttt.com/trigger/"+event+"/with/key/"+api_key
    response = ""
    try:
        tmout = 15
        response = requests.get(url = URL, files = DATA, timeout = tmout) 
    except:
	    response = "timeout waiting for IFTTT API response"  
    return(response)


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
  message = "Activity was seen "+ str(tot) +" times today"
  message += "\n\n"
  message += "ACTIVITY  DAY/MO  HOUR   COUNT\n"
  hasharray = collections.OrderedDict(sorted(hasharray.items(), key=lambda t: t[0]))
  for (name,val) in hasharray.items():
	message += str(name) + ":00 = "+ str(val) + "\n"
else:
  message = 'NO ACTIVITY SEEN TODAY'

message = "" + message + ""

status = sendifttt(message)

print "STATUS:"+str(status)+"\n"


