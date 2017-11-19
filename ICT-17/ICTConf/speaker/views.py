from django.shortcuts import render, get_object_or_404

# Create your views here.
from event.models import Event
from speaker.models import Speaker
from tickets.models import Tickets

ticket_count = Tickets.objects.all()
def Speakers(request):

    speakers = Speaker.objects.all()
    events = Event.objects.all()
    return render(request, "specindex.html", {"speakers":speakers,
                                          "events":events,"ticket_count":ticket_count.count()})

def Speaker_Detail(request, slug):

    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, "speaker_detail.html", {"speaker":speaker})
