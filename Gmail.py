import smtplib
import mimetypes
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
class Gmail:
    def sendMessage(recipientAddr, title, message):
        host = "smtp.gmail.com"
        port = "587"
        senderAddr = "csb2987@gmail.com"
        msg = MIMEMultipart()
        msg['Subject'] = title
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
        with open("picture.gif", 'rb') as f:
            part = MIMEImage(f.read())
            msg.attach(part)
        for str in message:
            part = MIMEText(str)
            msg.attach(part)
        s = smtplib.SMTP(host, port)
        # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr,"")
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()
