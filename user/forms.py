from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['isim', 'resim'] # gözükecek olan bilgiler
    
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'}) # attribute u updateledik


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
