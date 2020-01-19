from django.test import TestCase, RequestFactory
from blog.views import post_list
from .models import Event, Category
import json

class PostTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        request = self.factory.get('/')
        response = post_list(request)
        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NASA')

    def test_load_events(self):
        json_file = open('blog/test_data/wildfires.json').read()
        data = json.loads(json_file)
        events = data["events"]
        for event in events:
            Category.load_category(event)
            Event.load_event(event)
        events = Event.objects.all()
        self.assertEqual(20, events.count())

