from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url('^today/$',views.home,name='siteToday'),
    # url(r'^search/', views.search_results, name='search_results'),


]