from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=3000)
    publish_date = forms.DateField(required=False)
