from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url('^today/$',views.home,name='siteToday'),
    url('^profile/(\d+)', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^business/(\d+)',views.business,name ='business'),
    url(r'^new/', views.new_business, name='new_business'),
    url(r'^new/', views.new_hood, name='new_hood'),
    url(r'^new/post/$', views.post, name='post'),
    url(r'^contact',views.contact,name ='contact'),
    url(r'^location/(\d+)',views.location,name ='location'),
    url(r'^hood/(\d+)',views.hood,name ='hood')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
