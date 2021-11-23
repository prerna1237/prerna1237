#!/usr/bin/env python
import psutil
import smtplib
import subprocess
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

with open("/root/python-scripts/secrets.txt") as f:
    lines = f.readlines()
    gmail_password = lines[2].strip()

print("Below is the Workspace Usage: \n")
JobSize = subprocess.check_output(['du', '-sh', '/var/lib/jenkins/jobs']).decode('utf-8')
print(JobSize)
workspaceSize = subprocess.check_output(['du', '-sh', '/var/lib/jenkins/workspace']).decode('utf-8')
print(workspaceSize)
logSize = subprocess.check_output(['du', '-sh', '/var/lib/jenkins/logs']).decode('utf-8')
print(logSize)

msg = MIMEMultipart()
msg['From'] = 'prerna.gupta7321@gmail.com'
msg['To'] = 'prerna.gupta03@nagarro.com'
msg['Subject'] = 'WorkSpace Usage of Jenkins Machine'
body = "Below is the Workspace Usage: \n \n" + JobSize + "\n" + workspaceSize + "\n" + logSize
msg.attach(MIMEText(body,'plain'))

text = msg.as_string()
server1 = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server1.login('prerna.gupta7321@gmail.com', gmail_password)
server1.sendmail('prerna.gupta7321@gmail.com','prerna.gupta03@nagarro.com',text)
