from django.shortcuts import render,HttpResponse
from .models import  Event
import json

# Create your views here.


def events_to_json(request):
    events = Event.objects.all()
    event_dict_tmp = {}
    event_dict = []
    for obj in events:
        event_dict_tmp['id'] = obj.id
        event_dict_tmp['speaker'] = str(obj.speaker)
        event_dict_tmp['content'] = obj.content

        event_dict.append(event_dict_tmp)

    return HttpResponse(json.dumps({"data": event_dict}), content_type='application/json')
