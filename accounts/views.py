from django.shortcuts import render
from .forms import RegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.

class RegistrationView(CreateView):
    template_name = 'registration/registr.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    
