from .models import WebUser
from django import forms

class BookForm(forms.Form):
    fullname = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder":"FulltName"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
    username = forms.CharField(max_length=200)
    password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,)
    show = forms.DateField(required=False)
    show_passwor = forms.BooleanField()
    Gender = forms.TypedChoiceField( choices=(
        ("erkak","Male"),
        ("ayol", "Female")
    ))
    
    def save(self, commit=True):
        pass

class WebUserForm(forms.ModelForm):
    class Meta:
        model = WebUser
        fields =("full_name","email", "username", "password","show")