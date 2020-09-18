from django.shortcuts import render
from .models import Destination


# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Bangalore'
    dest1.desc = 'The bangalore is garden city'
    dest1.img = 'nature.jpg'
    dest1.prise = 88800

    dest2 = Destination()
    dest2.name = 'London'
    dest2.desc = 'The london is beautiful city'
    dest2.img = 'nature.jpg'
    dest2.prise = 100000

    dest3 = Destination()
    dest3.name = 'brazil'
    dest3.desc = 'the Brazil is most famouse country'
    dest3.img = 'nature.jpg'
    dest3.prise = 50000

    dests = [dest1, dest2, dest3]
    
    return render(request, "index.html", {'dests': dests})

