# -*- coding: UTF-8 -*-

from email.mime.text import MIMEText
from .config import *
import re
import logging
import smtplib
from django.core.mail.message import EmailMultiAlternatives



class MailSys():
    def __init__(self):
        ##default smtp server of uss.
        self.server = smtplib.SMTP("SMT_SERVER",PORT)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()
        self.server.login(config['mail_addr'],config['passwd'])
        self.mail_addr = config['mail_addr']


    def __str__(self):
        print("Mailing Server object :      {}".format(self))
        print("SMTP SERVER : smtp.yandex.com PORT : 587")
    def send_mail(self,name,to_addr):


        subject = "ICTCONF 17"
        text_content = '''   Sayın {} ICTCONF 17 de sizleri aramızda görmekten mutluluk duyacağız . '''.format(name)

        from_email, to = 'kayit@ictconf.net', '{}'.format(to_addr)
        html_content =  '''   <h1>Sayın {}</h1> <p>ICTCONF 17 de sizleri aramızda görmekten mutluluk duyacağız . </p>'''.format(name)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")

        try:
            msg.send()
            logging.debug("Mail Sent to the {}".format(to_addr))
            return True
        except:
            return False






    def support_mail_send(self, data, to_addr):

        content = ''' SUPPORT-REQUEST:{} Name : {} Surname : {} Content : {}  '''.format(to_addr,data['name'],data['surname'],data['content'])
        mail_text = MIMEText("{}".format(content))

        try:
            self.server.sendmail(self.mail_addr,to_addr,mail_text.as_string())
            logging.debug("Mail Sent to the {}".format(to_addr))
            return True
        except:
            return False
