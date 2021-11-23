import jenkins
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

with open("/root/python-scripts/secrets.txt") as f:
    lines = f.readlines()
    jenkins_username = lines[0].strip()
    jenkins_password = lines[1].strip()
    gmail_password = lines[2].strip()

server = jenkins.Jenkins('http://jenkins_username:jenkins_password@18.219.186.185:8080/', username=jenkins_username, password=jenkins_password)

nodes = server.get_nodes()
server1 = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server1.login('prerna.gupta7321@gmail.com', gmail_password)
for node in nodes:
  if node['offline'] == True:
    print(node['name'] +  " is in offline state")
    node_name = node['name']

    msg = MIMEMultipart()
    msg['From'] = 'prerna.gupta7321@gmail.com'
    msg['To'] = 'prerna.gupta03@nagarro.com'
    msg['Subject'] = 'Jenkins Node Status Report'

    body = """\
    <html>
    <head>
    <style>
    </style>
    </head>
    <body><p> {node_name}:<span style="color: red"> OFFLINE </span> </p>
    </body>
    </html>
    """.format(node_name=node_name)
    msg.attach(MIMEText(body,'html'))

    text = msg.as_string()

    server1.sendmail('prerna.gupta7321@gmail.com','prerna.gupta03@nagarro.com',text)
