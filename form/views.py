from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Person

def new(request):
    return render(request, 'form/form1.html')

def register(request):
    print request.POST['name'],request.POST['dob']
    obj = Person(name=request.POST['name'], DOB=request.POST['dob'])
    obj.save()
    return HttpResponseRedirect(reverse('form:home'))

def home(request):
    plist = Person.objects.all()
    context = {"person_list":plist}
    return render(request, 'form/home.html', context)

def person_detail(request, person_id):
    obj = get_object_or_404(Person, pk=person_id)
    context = {'person':obj}
    return render(request, 'form/details.html', context)
    