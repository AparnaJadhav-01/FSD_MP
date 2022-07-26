from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'apts'
urlpatterns=[
    path('',views.home,name='home'),
    path('search/', views.searchform, name='searchform'),
]