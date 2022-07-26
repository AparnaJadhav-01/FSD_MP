from django.db import models
from django.db.models import Q
from django.shortcuts import render, redirect
from listings import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def home(request):

    rep1 = models.Listing.objects.order_by('-list_date')[0:3]
    context={
        'listings':rep1
    }
    return render(request, 'apts/home.html',context)

def fav_post(request,id):  #------------------------add/ remove post
    post=get_object_or_404(models.Listing,id=request.GET.get('post_id'))
    if post.fav.filter(id=request.user.id).exists():
        post.fav.remove(request.user)                 
    else:
        post.fav.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())

def favorites(request,id): #---------------------handles button display
    listing = models.Listing.objects.all()
    print("id",id)
    is_fav= False     
    post=get_object_or_404(models.Listing,id=id)
    if post.fav.filter(id=request.user.id).exists():
        is_fav=True
        # context = {
        #   'listing': listing,
        #       'fav_post':is_fav,
        #      }
        # return render(request, 'apts/showflat.html', context)
    user=request.user
    fav_post=user.fav.all()
    return render(request,'accounts/fav.html',{'fav_post':fav_post})

def dirfav(request):  
    user=request.user
    fav_post=user.fav.all()
    return render(request,'accounts/fav.html',{'fav_post':fav_post})



def searchform(request):
    queryset_list = models.Listing.objects.order_by('-list_date')

    if 'bedroom' in request.GET:
        bed = request.GET['bedroom']
        if bed:
          queryset_list = queryset_list.filter(bedrooms=bed)

    if 'rent' in request.GET:
        price = request.GET['rent']
        print("------------------------------------")
        print("------------------------------------")
        print("------------------------------------")
        print("------------------------------------")
        print("------------------------------------")
        print(price,type(price))
        if price:
          price = int(request.GET['rent'])
          queryset_list = queryset_list.filter(price__lte=price)
          print(price)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
          queryset_list = queryset_list.filter(city=city)
   
    furniture=request.GET.get('furnished')
    parking_lot=request.GET.get('parking')

    if furniture == 'on':
        furniture = True
        q4=Q(is_furnished= furniture)
        q6=Q(is_furnished= furniture)
    else:
        furniture = False
        q4=Q(is_furnished= furniture)
        furniture = True
        q6=Q(is_furnished= furniture)

    if parking_lot == 'on':
        parking_lot = True
        q5=Q(park_lot=parking_lot)
        q7=Q(park_lot=parking_lot)
    else:
        parking_lot = False
        q5=Q(park_lot=parking_lot)
        parking_lot = True
        q7=Q(park_lot=parking_lot)
    
    
        
    queryset_list=queryset_list.filter(q5 | q7)
    queryset_list=queryset_list.filter(q4 | q6)
    print("hiiiiiiiiiiiii\n",q4,q5,q6)
    context ={
      'filter':queryset_list
    }
    return render(request, "apts/searchflat.html",context)