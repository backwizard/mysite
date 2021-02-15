from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=50)
    last_name = forms.CharField(label='Your last name', max_length=60)
    phone_number = forms.CharField(max_length=10)
    email = forms.EmailField(max_length=50)
