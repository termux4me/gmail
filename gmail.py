#!/usr/bin/env python
import time
print'||||||||||||||||||||||||||||||||||||||||||||||||'
print'|||||||||||||||starting   server|||||||||||||||||'
print'||||||||||||||||||||||||||||||||||||||||||||||||||'
time.sleep(3)
print' '
print' '
print'|=====================================|'
print'|         .....................       |'     
print'|         :mostakhdim facebook:       |'
print'|         :...................:       |'  
print'|                                     |'
print'|        send email with GMAIL.py     |'
print'|                                     |'  
print'|_____________________________________|'  
print'|∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆∆|'
print' '
print' '
time.sleep(2)
print'***************************************************'
import smtplib
fromaddr=raw_input('from ')
print'***************************************************'
to=raw_input('to: ')
print'***************************************************'
subject=raw_input('subject ')
print'***************************************************'
message=raw_input('Message: ')
print'***************************************************'
password=raw_input('\npassword: ')
print'***************************************************'
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr,password)
server.sendmail(fromaddr,to,message,subject)
print'•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•'
print'                         Done'
print'•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•°•'
server.quit()
