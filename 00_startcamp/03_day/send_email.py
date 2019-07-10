import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

msg = EmailMessage()
msg['Subject'] = '합격_통지서'
msg['From'] = 'koi4553@naver.com'
msg['To'] = '@gmail.com'
msg.set_content('축.하 ^오^')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('koi4553', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')