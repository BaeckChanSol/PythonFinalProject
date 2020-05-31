import smtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import mimetypes

class Gmail:
    def sendMeesage(recipientAddr, message):
        host = "smtp.gmail.com"
        port = "587"
        senderAddr = "아이디"
        msg = MIMEBase("multipart", "alternative")
        msg['Subject'] = message
        msg['From'] = senderAddr
        msg['To'] = recipientAddr
        s = smtplib.SMTP(host, port)
        # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(senderAddr,"비번")
        s.sendmail(senderAddr, [recipientAddr], msg.as_string())
        s.close()


