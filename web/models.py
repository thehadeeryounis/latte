from django.db import models
from django.contrib.auth.models import User, UserManager
from datetime import datetime
from taggit.managers import TaggableManager
from accounts.models import UserenaBaseProfile
from django.core.urlresolvers import reverse

class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User, unique=True, verbose_name=('user'), related_name='my_profile')
    GENDER_CHOICES = ((1, ('Male')),(2, ('Female')),)

    gender = models.PositiveSmallIntegerField(('gender'),
                                              choices=GENDER_CHOICES,
                                              blank=True,
                                              null=True)

    website = models.URLField(('website'), blank=True, verify_exists=True)
    location =  models.CharField(('location'), max_length=255, blank=True)
    birth_date = models.DateField(('birth date'), blank=True, null=True)
    about_me = models.TextField(('about me'), blank=True)

    @property
    def age(self):
        if not self.birth_date: return False
        else:
            today = datetime.date.today()
            # Raised when birth date is February 29 and the current year is not a
            # leap year.
            try:
                birthday = self.birth_date.replace(year=today.year)
            except ValueError:
                day = today.day - 1 if today.day != 1 else today.day + 2
                birthday = self.birth_date.replace(year=today.year, day=day)
            if birthday > today: return today.year - self.birth_date.year - 1
            else: return today.year - self.birth_date.year

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

class MyCustomModel(LatteModel):
    name = models.CharField(max_length=50, null = False, blank = False)
    time_stamp = models.DateTimeField('date created')
    description = models.CharField(max_length=200, null = True, blank = True)
    repository_url = models.CharField(max_length=100, null = True, blank = True, unique = True)
    slug = models.CharField(max_length=20, unique = True)
    tags = TaggableManager()
    owner = models.ForeignKey(User)
    members = models.ManyToManyField(User, related_name='members')