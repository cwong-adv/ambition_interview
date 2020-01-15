from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from entity.sync import sync_entities
import json

from .models import Event
from .tasks import fetch_url

URLS = ["https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories/8?limit=20",
        "https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories/10?limit=20",
        "https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories/18?limit=20",
        "https://eonet.sci.gsfc.nasa.gov/api/v2.1/categories/6?limit=20"]


# Create your views here.
def post_list(request):
    for url in URLS:
        fetch_url.delay(url)
    #sync_entities()
    events = Event.objects.all()
    return render(request, 'blog/post_list.html', {'posts': events})

def event_api(request):
    events = Event.objects.all()
    event_list = serializers.serialize('json', events)
    response = '{"event_list":' + event_list + '}'
    return HttpResponse(response, content_type="application/json")

def task_state(request):
    data = 'Fail'
    if request.is_ajax():
        if 'task_id' in request.POST.keys() and request.POST['task_id']:
            task_id = request.POST['task_id']
            task = AsyncResult(task_id)
            data = task.result or task.state
        else:
            data = 'No task_id in the request'
    else:
        data = 'This is not an ajax request'

    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')