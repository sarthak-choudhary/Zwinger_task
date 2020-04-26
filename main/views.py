from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from main.utils import get_current_location, sort_toilets
from main.models import Toilet

def index(request):
    return render(request, 'index.html')

def add_toilet(request):
    toilet = Toilet()
    toilet.lat, toilet.lon = get_current_location()

    toilet.save()
    
    return redirect(reverse('main:index'))


def get_toilets(request):

    nearby_toilets = sort_toilets(list(Toilet.objects.all()))
    lat, lon = get_current_location()
    your_location = {
        'lat': lat,
        'lon': lon
    }
    context = {'toilets': nearby_toilets,
                'your_location': your_location }
    return render(request, 'nearby_toilets.html', context = context)