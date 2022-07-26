from django.db import models
from django.db.models import Q
from django.shortcuts import render, redirect
from listings import models
from apts.filters import AptFilter
# from .choices import price_choices, bedroom_choices, state_choices

# Create your views here.

def home(request):

    rep1 = models.Listing.objects.all()
    context={
        'listings':rep1
    }
    return render(request, 'apts/home.html',context)


# def searchform(request):
#     qs = models.Listing.objects.all()
#     filt= AptFilter(request.GET,queryset=qs)
#     print ("hiii\nhiiii\nhiiiii\nhiiii")
#     context ={
#       'filter':filt
#     }
#     print(filt.qs)
#     return render(request, "apts/searchflat.html",context)

def searchform(request):
    rooms = request.GET.get('bedroom', None)
    price = request.GET.get('rent', None)
    city = request.GET.get('city', None)

    print(rooms,price,city)

    apartments = models.Listing.objects.all()
    q1=Q(price__lte=price) 
    q2=Q(bedrooms=rooms)
    q3=Q(city=city)
    print(q1,q2,q3 ,"queryyyyy")
    qs=apartments.filter(q1 & q2 & q3)
    print(qs)
    
    print("hiiiiiiiiiiiii\n",qs)
    context ={
      'filter':qs
    }
    return render(request, "apts/searchflat.html",context)