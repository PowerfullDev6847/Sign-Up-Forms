from django import forms

class BookForm(forms.Form):
    FullName = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"placeholder":"FulltName"}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
    Username = forms.CharField(max_length=200)
    Passwor = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput,)
    Show = forms.DateField(required=False)
    Show_Passwor = forms.BooleanField()
    Gender = forms.TypedChoiceField( choices=(
        ("erkak","Male"),
        ("ayol", "Female")
    ))
    