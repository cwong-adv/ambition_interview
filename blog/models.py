from django.conf import settings
from django.db import models
from django.utils import timezone
from entity.config import register_entity, EntityConfig


class Category(models.Model):
    category_id = models.IntegerField()
    category_title = models.CharField(max_length=200, unique=True)

    def load_category(event):
        category_id = event["categories"][0]["id"]
        category_title = event["categories"][0]["title"]
        new_category, created = Category.objects.get_or_create(category_id=category_id, category_title=category_title)

    def __str__(self):
        return "%s | %s " % (self.category_title, self.category_id)

class Event(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=timezone.now)

    def load_event(event):
        from blog.models import Category

        category_id = event["categories"][0]["id"]
        event_name = event["title"]
        event_date = event["geometries"][0]["date"]

        new_event, created = Event.objects.get_or_create(category=Category.objects.get(category_id=category_id),
                                                         event_name=event_name,
                                                         event_date=event_date)

    def __str__(self):
        return "%s | %s " % (self.event_name, self.event_date)

@register_entity()
class CategoryConfig(EntityConfig):
    queryset = Category.objects.all()

@register_entity()
class EventConfig(EntityConfig):
    queryset = Event.objects.all()

    #def get_super_entities(self, model_objs):
        #return {
            #Category: [(model_obj.id, model_obj.category_title) for model_obj in model_objs]
        #}
