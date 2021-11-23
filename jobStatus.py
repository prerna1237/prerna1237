import json
import requests
import time
import datetime
import smtplib
import jenkins
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

with open("/root/python-scripts/secrets.txt") as f:
    lines = f.readlines()
    jenkins_username = lines[0].strip()
    jenkins_password = lines[1].strip()
    gmail_password = lines[2].strip()

msg = MIMEMultipart()
msg['From'] = 'prerna.gupta7321@gmail.com'
msg['To'] = 'prerna.gupta03@nagarro.com'

server = jenkins.Jenkins('http://jenkins_username:jenkins_password@18.219.186.185:8080/', username=jenkins_username, password=jenkins_password)
total_jobs = server.jobs_count()
#print(total_jobs)
jobs = server.get_jobs()
for i in range(total_jobs):
  jobname = jobs[i]['name']
  info = server.get_job_info(jobname)
  builds = info['builds']
  for build in builds:
                buildinfo = server.get_build_info(jobname,build['number'])
                buildno = buildinfo['number']
                buildnumber = str(buildno)
                url  = "http://" + jenkins_username + ":" + jenkins_password + "@18.219.186.185:8080/job/" + jobname + "/" + buildnumber + "/api/json"    #Replace 'your_jenkins_endpoint' with your Jenkins URL
                url1 = "http://" + jenkins_username + ":" + jenkins_password + "@18.219.186.185:8080/job/"  + jobname + "/" + buildnumber + "/buildTimestamp"
                data = requests.get(url).json()
                data1 = requests.get(url1)
                data2 = data1.content
                data3 = data2.decode("utf-8")

                format = '%m/%d/%y %H:%M %p'
                format1 = '%m/%d/%y %H:%M:%S'
                startDateTime = datetime.datetime.strptime(data3, format)
                linuxDate = time.strftime("%m/%d/%y %H:%M:%S")
                endDateTime = datetime.datetime.strptime(linuxDate, format1)
                diff = endDateTime - startDateTime
                totalSecond = int(diff.total_seconds())

                if data['building'] and totalSecond > 60:
                  print("Job is running and pending since last 1 mins: " + jobname + " " + buildnumber)

                  msg['Subject'] = 'Job in Pending State | Job Name: ' + jobname + ' | Build Number: ' + buildnumber
                  body = 'Job is running and pending since last 1 mins \n Job Name:' + jobname + '\n Build Number: ' +buildnumber
                  msg.attach(MIMEText(body,'plain'))
                  text = msg.as_string()
                  server1 = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                  server1.login('prerna.gupta7321@gmail.com', gmail_password)
                  server1.sendmail('prerna.gupta7321@gmail.com','prerna.gupta03@nagarro.com',text)
                  server1.quit()

                else:
                  print("Job is completed: " + jobname + " " + buildnumber)

