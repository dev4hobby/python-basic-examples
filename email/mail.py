import os
import smtplib
from dotenv import load_dotenv
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

load_dotenv() # load `.env`

class Driver():
    def __init__(self):
        self.mail_fname = None
        self.mail_user = None
        self.mail_pwd = None

class Gmail(Driver):
    def __init__(self):
        self.mail_fname = os.getenv('GMAIL_FNAME')
        self.mail_user = os.getenv('GMAIL_USER_ID')
        self.mail_pwd = os.getenv('GMAIL_USER_PW')

    def send(self, to, subject, html_body, attach):
        msg = MIMEMultipart(_subtype='related')
        msg['Form']='"%s"<%s>' % (self.mail_fname, self.mail_user)
        msg['To'] = to
        msg['Subject'] = Header(s=subject, charset="utf-8")

        # attach body
        body = MIMEText(html_body, _subtype='html')
        msg.attach(body)

        # attach image
        img_data = open('./frog.jpg', 'rb').read()
        img = MIMEImage(img_data, 'jpeg')
        img.add_header('Content-id', '<image0001.png>')
        msg.attach(img)

        # send
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #server.set_debuglevel(1) # SMTP debug level
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.mail_user, self.mail_pwd)
        ret = server.sendmail(self.mail_user, to, msg.as_string())
        server.close()
        return ret 