#!/usr/bin/env python
import psutil
import smtplib
import subprocess
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

gmail_password = sys.argv[1]

# gives a single float value
cpuUsage = psutil.cpu_percent(10)

ramUsage = psutil.virtual_memory()[2]


msg = MIMEMultipart()
msg['From'] = 'prerna.gupta7321@gmail.com'
msg['To'] = 'prerna.gupta03@nagarro.com'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('prerna.gupta7321@gmail.com', gmail_password)

if cpuUsage > 10:
  print("CPU utilization is above the minimal value i.e. " + str(cpuUsage))

  msg['Subject'] = 'Jenkins CPU Utilization above threshold'
  body = 'CPU utilization is above the minimal value i.e. ' + str(cpuUsage)
  msg.attach(MIMEText(body,'plain'))
  text = msg.as_string()
  server.sendmail('prerna.gupta7321@gmail.com','prerna.gupta03@nagarro.com',text)

else:
  print("CPU utilization is below the minimal value i.e. " + str(cpuUsage))

if ramUsage > 10:
  print("Memory Usage is above the minimal value i.e. " + str(ramUsage))

  msg['Subject'] = 'Jenkins Memory Usage above threshold'
  body = 'Memory Usage is above the minimal value i.e. ' + str(ramUsage)
  msg.attach(MIMEText(body,'plain'))
  text = msg.as_string()
  server.sendmail('prerna.gupta7321@gmail.com','prerna.gupta03@nagarro.com',text)

else:
  print("Memory Usage is below the minimal value i.e. " + str(ramUsage) + "\n")


