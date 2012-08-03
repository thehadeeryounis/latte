from django import forms
from web.models import Profile

from userprofiles.forms import RegistrationForm

class ProfileRegistrationForm(RegistrationForm):

    def save_profile(self, new_user, *args, **kwargs):
        Profile.objects.create( user=new_user)