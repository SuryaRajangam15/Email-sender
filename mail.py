import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'prashanthlrp03@gmail.com'
msg['To'] = 'suryarajangam001@gmail.com'
msg['Subject'] = 'simple email in python 3'
message = 'This is a sample message generated using a automatics sender email '
msg.attach(MIMEText(message))


def SendEmail(From, to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()  # identify ourselves to smtp gmail client
        server.starttls()  # secure our email with tls encryption
        server.login(From, 'Prashanth@37')  # Update your Email password here!
        server.sendmail(From, to, content)
        print("Mail Sent Successfully!")
    except:
        print("Error occurred while sending mail")


SendEmail(msg['From'], msg['To'], msg.as_string())