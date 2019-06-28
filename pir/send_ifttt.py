#!/usr/bin/python
# Sends email daily 
# Run by crontab

import sys
import collections
import requests 


# IFTTT ACCOUNT INFO
api_key  = "{your_api_key}" # Your API KEY from https://ifttt.com/maker
event    = "morning_message"       # IFTTT Event ID

# IFTTT limits SMS to ~80 chrs
useSMS   = 1               # 1 = SMS, 0 = email


#################
# SEND IFTTT
def sendifttt(message):
    DATA = { 'value1' : message }
    URL = "https://maker.ifttt.com/trigger/"+event+"/with/key/"+api_key
    response = ""
    try:
        tmout = 30
        response = requests.get(url = URL, data = DATA, timeout = tmout) 
    #print DATA # Uncomment to Debug
    except:
        response = "timeout waiting for IFTTT API response"  
    return(response)


#################
# MAIN
#################

# GET ACTIVITY FOR TODAY
newline   = "<br>"
hasharray = {} 
message   = ""

  
try:
  tot = 0;

  # TOTAL UP ACTIVITY COUNTS BY HOUR
  with open('daily.log') as f:
    for line in f:
      dayhour = line[12:20]
      if not dayhour in hasharray:
        hasharray[dayhour] = 1
      else:
        hasharray[dayhour] += 1
      tot += 1
except:
  #print "debug error:", sys.exc_info()[0]
  tot = 0;


# BUILD THE MESSAGE
if (tot > 0):
  message = "Activity seen "+ str(tot) +" times"
  message += newline
  hasharray = collections.OrderedDict(sorted(hasharray.items(), key=lambda t: t[0]))
  if useSMS:  # Limit to just last few entries due to SMS limits
    last = list(hasharray.items())
    max  = len(last) 
    for x in range(max-1, max-5, -1):
        (name,val) = last[x]
    message += str(name) + ":00 = "+ str(val) + newline
  else:  
    for (name,val) in hasharray.items():
    message += str(name) + ":00 = "+ str(val) + newline
else:
  # IS THIS A REBOOT MESSAGE?
  if len(sys.argv) > 1:
    message = 'PIR SENSOR RESTARTED'
  else:
    message += 'NO ACTIVITY SEEN TODAY'

message = "" + message + ""

# Limit msg size for SMS
if useSMS:
   message = message[0:81] 

status = sendifttt(message)

print "STATUS:"+str(status)+"\n"
if '200' in str(status):
    print "SUCCESS"
else:
    print "IFTTT ERROR"

