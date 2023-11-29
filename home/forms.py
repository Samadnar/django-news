from django import forms

from .models import News, Contact
class AddNewForms(forms.ModelForm):
   class Meta:
       model = News
       fields = ['title', 'img', 'body', 'category', 'tags']
       
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'message')
        