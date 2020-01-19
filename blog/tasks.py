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

        new_category, created = Category.objects.get_or_create(category_id=category_id, category_title=category_title)
        new_event, created = Event.objects.get_or_create(category=Category.objects.get(category_id=category_id),
                                                         event_name=event_name,
                                                         event_date=event_date)





