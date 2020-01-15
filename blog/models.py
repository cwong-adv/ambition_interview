from django.conf import settings
from django.db import models
from django.utils import timezone
from entity.config import register_entity, EntityConfig


class Category(models.Model):
    category_id = models.IntegerField()
    category_title = models.CharField(max_length=200)

    def __str__(self):
        return "%s | %s " % (self.category_title, self.category_id)

class Event(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=timezone.now)

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
            #Category: [(model_obj.id, model_obj.group_id) for model_obj in model_objs]
       # }
