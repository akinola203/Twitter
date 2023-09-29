
from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Post
from .models import Profile

class UserRegisterForm(UserCreationForm):

      class Meta:
            model = User
            fields = ['first_name', 'username','email','password1','password2']


      def __init__(self, *args: Any, **kwargs: Any) -> None:
          super(UserRegisterForm, self).__init__(*args, **kwargs)


          for fieldname in ('username', 'password1', 'email','password2'):
            self.fields[fieldname].help_text = None

class PostForm(forms.ModelForm):
     content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100',
                                                             'id':'contentsBox','rows':'3',
                                                             'placeholder':'What is Happening?'})) 
                                                               
     
     class Meta:
          model = Post
          fields = ['content']





class UserUpdateForm(forms.ModelForm):
     class Meta:
          model = User
          fields = ['first_name','username']

class ProfileUpdateForm(forms.ModelForm):
     class Meta:
          model = Profile
          fields = ['image','bio']


