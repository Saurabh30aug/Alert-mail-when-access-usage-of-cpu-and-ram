import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import psutil
psutil.cpu_percent()
psutil.virtual_memory()
dict(psutil.virtual_memory()._asdict())
ram_used=psutil.virtual_memory().percent
avl_mem=psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
if(ram_used>50 and avl_mem<50):
    email_user = 'your email id'
    email_password = 'your password'
    email_send = 'to whom you want to send an email'

    subject = 'Message From Saurabh to Timble Technology'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Here is the message from saurabh you have been Sent an Email as Cpu and Ram Usage is more than 50%!'
    msg.attach(MIMEText(body, 'plain'))

    filename = 'warning.pdf'
    attachment = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()

else:
    print('No need Sent an Email as Cpu and Ram Usage is less than 50% ')









