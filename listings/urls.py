from django.urls import path

from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.index),
    path('listingfun', views.listingfun,name='listingfun'),
    path('apt/<listing_title>', views.listinggo,name='listinggo'),
    path('search', views.search, name='search'),
]