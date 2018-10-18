from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

def welcome(request):
    date = dt.date.today()

    return render(request, 'welcome.html', {"date": date,})
