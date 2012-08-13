from django.db import models
from django.contrib.auth.models import User, UserManager
from datetime import datetime
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView

class Profile(models.Model):
    user = models.OneToOneField(User)
    short_info = models.TextField(blank=True)

class LatteModel(models.Model):
    class Meta:
        abstract = True

    def json( self ):
        return serializers.serialize( 'json', [self] )

    def get_absolute_url(self):
        return reverse(self.__class__.__name__.lower()+"-details",kwargs={'pk': self.pk})

    def __str__(self):
        try:
            return self.name
        except:
            try:
                return self.description
            except:
                return str(self.number)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Item(LatteModel):
    name = models.CharField(max_length=50, null = False, blank = False)

