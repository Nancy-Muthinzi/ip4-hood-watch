from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url('^today/$',views.home,name='siteToday'),
    url('^profile/(\d+)', views.profile, name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^business/(\d+)',views.business,name ='business')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
