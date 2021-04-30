from django.shortcuts import render
from django.views.generic import ListView
from myclientapp.models import Person

# Create your views here.
class Person_Listview(ListView):
    model=Person
    template_name='person.html'
    context_object_name='persons'
