# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
import json

from .models import Event, Category


@shared_task
def fetch_url(url):
    resp = requests.get(url)
    data = json.loads(resp.text)
    events = data["events"]
    for e in events:
        category_id = e["categories"][0]["id"]
        category_title = e["categories"][0]["title"]
        event_name = e["title"]
        event_date = e["geometries"][0]["date"]

        if not Category.objects.filter(category_id=category_id):
            new_category = Category(category_id=category_id,
                                    category_title=category_title)
            new_category.save()

        if not Event.objects.filter(event_name=event_name):
            new_event = Event(event_name=event_name,
                              event_date=event_date)
            new_event.save()




