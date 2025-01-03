from attr import field
from django import forms
from django.contrib.auth.models import User

from .models import Location,Profile
from .widgets import CustomPictureImageFieldWidget

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name',)

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number','email')
