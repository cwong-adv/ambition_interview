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
    for event in events:
        Category.load_category(event)
        Event.load_event(event)






