from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Admin, Hood

def home(request):
    date = dt.date.today()

    return render(request, 'home.html', {"date": date,})

def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})