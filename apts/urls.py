from django.urls import path,include
from . import views
from django.conf.urls import url

app_name = 'apts'
urlpatterns=[
    path('',views.home,name='home'),
    path('search/', views.searchform, name='searchform'),
    url(r'(?P<id>\d+)/fav_post/$',views.fav_post,name='fav_post'),
    url(r'(?P<id>\d+)/favorites/', views.favorites, name='favorites'),
    path('dirfav/', views.dirfav, name='dirfav'),
    path('listings/',include('listings.urls')),
]