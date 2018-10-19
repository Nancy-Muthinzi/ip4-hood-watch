from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Hood, Profile, Business
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()

    return render(request, 'home.html', {"date": date,})

@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    # profile = Profile.objects.get(user=current_user)
    profile = Profile.objects.get()

    return render(request, 'profile.html', {'profile':profile})    

@login_required(login_url='/accounts/login/')
def business(request, hood_id):
    try:
        business = Business.objects.get(id = hood_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"business.html", {"business":business})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})