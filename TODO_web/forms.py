from django import forms
from .models import consumers,Todo
from django.forms.renderers import TemplatesSetting
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User 

class consumerForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'input1','placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'input1','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ['id','username', 'email','password1','password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class':'input1','placeholder':'Username'}),
            'email' : forms.TextInput(attrs={'class':'input1','placeholder':'email'}),
            
        }


        # def __init__(self,*args,**kwargs):
        #     super().__init__(*args,**kwargs)
            
        #     self.fields['username'].widget.attrs.update({'class':'input1','placeholder':'username'})
            

class loginForm(UserCreationForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'input1','placeholder':'Enter Password'}))
    class Meta:
        model = User
        fields = ['username','password']

        widgets = {
            'username' : forms.TextInput(attrs={'class':'input1','placeholder':'Username'}),
        }


class todoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['consumer','task']

        

        widgets = {
            'task' : forms.Textarea(attrs={'class':'text-field','placeholder':'Enter New Task...','rows':'1','id':'txtArea','onKeyUp':'SetNewSize(this)'}),
        }

class store_editTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['consumer','task']

        

        widgets = {
            'task' : forms.Textarea(attrs={'class':'text-field','placeholder':'Enter New Task...','rows':'1','id':'txtArea','onKeyUp':'SetNewSize(this)'}),
        }