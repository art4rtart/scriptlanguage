# -*- coding: cp949 -*-
import smtplib #Import smtplib for the actual sending function

from email.mime.text import MIMEText

smtpHost = "smtp.test.com"   #smtp ���� �ּ�

text = "hello world"
msg = MIMEText(text)  #�ؽ�Ʈ�� �⺻�� ������ �ϳ� �����մϴ�. text�� �ݵ��� ASCII�ڵ忩�߸� �մϴ�. ���� unicode�� ��� �ִٸ� �޴� �ʿ��� ���ڰ� �����ִ� ������ �ް� �� �� �Դϴ�.

senderAddr = "test@send.com"     #������ ��� email �ּ�.
recipientAddr = "test@rec.com"   #�޴� ��� email �ּ�.

msg['Subject'] = "test email"
msg['From'] = senderAddr
msg['To'] = recipientAddr

#SMTP ������ �̿��� ���� �����ϴ�.
s = smtplib.SMTP(smtpHost)
s.connect()
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()
