from django.shortcuts import render
from speaker.models import *
from event.models import *
from tickets.models import *
from gallery.models import *

from sponsorship.models import *

ticket_data = Tickets.objects.all()


# Create your views here.
def index(request):

    speaker_data = Speaker.objects.all()
    event_data = Event.objects.all()
    gallery_data = Gallery.objects.all()

    platin_sponsorship = SponsorShip.objects.filter(level_id=1)
    golden_sponsorship = SponsorShip.objects.filter(level_id=2)
    silver_sponsorship = SponsorShip.objects.filter(level_id=3)
    support_sponsorship = SponsorShip.objects.filter(level_id=4)
    media_sponsorship = SponsorShip.objects.filter(level_id=5)
    
    return render(request,"index.html",{"gallery_data":gallery_data,"speaker_data":speaker_data,"event_data":event_data,"platin":platin_sponsorship,"golden":golden_sponsorship,"silver":silver_sponsorship,"support":support_sponsorship,"media":media_sponsorship,"current_count":ticket_data.count()})
def contact(request):
    return render(request,"contact.html",{"current_count":ticket_data.count()})


def about(request):
    speaker_data = Speaker.objects.all()
    gallery_data = Gallery.objects.all()
    return render(request,"about.html",{"gallery_data":gallery_data,"speaker_data":speaker_data,"current_count":ticket_data.count()})

def schedule(request):
    speaker_data = Speaker.objects.all()
    event_datas = Event.objects.all()
    return render(request,"schedule.html",{"speaker_data":speaker_data,"event_datas":event_datas,"current_count":ticket_data.count()})



def get_ticket(request):
    return render(request,"get_ticket.html")
