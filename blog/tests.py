from django.test import TestCase, RequestFactory
from blog.views import post_list

class PostTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page(self):
        request = self.factory.get('/')
        response = post_list(request)
        self.assertEqual(response.get('content-type'), 'text/html; charset=utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'NASA')
