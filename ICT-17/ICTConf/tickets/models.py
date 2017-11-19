from django.core.exceptions import ValidationError
from django.db import models
import re

class Tickets(models.Model):

    participant_name = models.CharField(max_length=40)
    participant_surname = models.CharField(max_length=40)
    participant_mail_addr = models.EmailField(max_length=30,unique=True)


    def __str__(self):
        return "Name : {} {} ".format(self.participant_name,self.participant_surname)



    def mail_validation(self):

        if re.search("([A-z-0-9])*@*[A-z]*[.][a-z]*", self.participant_mail_addr) == None:
            return False
        else:
            return True




