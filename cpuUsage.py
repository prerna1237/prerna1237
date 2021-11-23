#!/usr/bin/env python
import psutil
import smtplib
import subprocess
import sys

gmail_password = sys.argv[1]

# gives a single float value
cpuUsage = psutil.cpu_percent(10)

ramUsage = psutil.virtual_memory()[2]

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('prerna.gupta7321@gmail.com', gmail_password)

if cpuUsage > 85:
  print("CPU utilization is above the minimal value i.e. " + str(cpuUsage))
  server.sendmail('prerna.gupta7321@gmail.com','prerna.gupta03@nagarro.com', 'CPU utilization is above the minimal value i.e. ' + str(cpuUsage))
else:
  print("CPU utilization is below the minimal value i.e. " + str(cpuUsage))
if ramUsage > 70:
  print("Memory Usage is above the minimal value i.e. " + str(ramUsage))
  server.sendmail('prerna.gupta7321@gmail.com','prerna.gupta03@nagarro.com','Memory Usage is above the minimal value i.e. ' + str(ramUsage))
else:
  print("Memory Usage is below the minimal value i.e. " + str(ramUsage) + "\n")
