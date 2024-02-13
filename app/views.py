from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
class SchoolList(ListView):
    model=School
    context_object_name='Schools'
    ordering=['scname']

class schooldetail(DetailView):
    model=School
    context_object_name='scl'
    ordering=['scname']

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
    

class SchoolDelete(DeleteView):
    model=School
    context_object_name='Sclo'
    success_url=reverse_lazy('SchoolList')
