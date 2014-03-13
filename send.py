import smtplib
from smtplib import SMTP
from email.mime.text import MIMEText

def send_message_via_smtp():
    smtp = SMTP('smtp.mailgun.org', 587)
    smtp.login('postmaster@caesarsgame.com', '3hmfbgj0iis2')
    msg = "hello world this is a test mail"
    msg = MIMEText(msg)
    smtp.sendmail('lhr@caesarsgame.com', "gameuser@caesarsgame.com", msg.as_string())
    smtp.quit()

send_message_via_smtp()

