from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('api', views.event_api, name='event_api'),
    path('sql_api', views.sql_api, name='sql_api')
]