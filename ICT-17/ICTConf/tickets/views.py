from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Tickets
import logging
from .mails import MailSys


ticket_data = Tickets.objects.all()
@require_http_methods(["POST"])
def validate_participant(request):
    new_participant = Tickets()


    new_participant.participant_name = request.POST.get('isim', ' ')
    new_participant.participant_surname = request.POST.get('soy_isim', ' ')

    new_participant.participant_mail_addr = request.POST.get('mail_adresi', ' ')
    

    new_mail_instance = MailSys()    
    if new_participant.mail_validation() == False:

        print(new_participant.participant_mail_addr)
        print("Invalid Email")
    else:
        try:
            new_participant.save()
            new_mail_instance = MailSys()
            new_mail_instance.send_mail(new_participant.participant_name, new_participant.participant_mail_addr)
	        
            return render(request, "index.html",{"mail_record_status":True,"current_count":ticket_data.count()})

        except:
            print("Mail Already allocated! ")
            return render(request, "index.html",{"mail_status":True})




    return render(request,"index.html")

@require_http_methods(["POST"])
def send_mail(request):
    name = request.POST.get('isim', ' ')
    surname = request.POST.get('soyisim', ' ')

    mail_addr = request.POST.get('mail_adresi', ' ')
    content = request.POST.get('text', ' ')

    new_mail_instance = MailSys()

    data = {}
    data['name'] = name
    data['surname'] = surname
    data['content'] = content
    data['mail_addr'] = mail_addr
    try:
        new_mail_instance.support_mail_send(data,'STUFF_MAIL_ADDR')

        return render(request, "index.html")
    except:
        print("Mail Sent Cannot Create ! ")
    ###sending_mail


@require_http_methods(["GET"])
def bulten(request):
    return render(request, "index.html")
