# -*- coding: cp949 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

#global value
host = "smtp.gmail.com" # Gmail STMP ���� �ּ�.
port = "587"
htmlFileName = "logo.html"

senderAddr = "mil*****@gmail.com"     # ������ ��� email �ּ�.
recipientAddr = "mi****@naver.com"   # �޴� ��� email �ּ�.

msg = MIMEBase("multipart", "alternative")
msg['Subject'] = "Test email in Python 3.0"
msg['From'] = senderAddr
msg['To'] = recipientAddr

# MIME ������ �����մϴ�.
htmlFD = open(htmlFileName, 'rb')
HtmlPart = MIMEText(htmlFD.read(),'html', _charset = 'UTF-8' )
htmlFD.close()

# ������� mime�� MIMEBase�� ÷�� ��Ų��.
msg.attach(HtmlPart)

# ������ �߼��Ѵ�.
s = mysmtplib.MySMTP(host,port)
#s.set_debuglevel(1)        # ������� �ʿ��� ��� �ּ��� Ǭ��.
s.ehlo()
s.starttls()
s.ehlo()
s.login("milkelf.choi@gmail.com","**********")
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()








































