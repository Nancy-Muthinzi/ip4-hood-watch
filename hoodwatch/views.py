from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime as dt
from .models import Hood, Profile, Business, Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm


@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    business = Business.objects.all()
    profiles = Profile.objects.all()
    posts = Post.objects.all()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = PostForm()

    return render(request, 'home.html', {'date': date, 'profile':profiles, 'postForm': form, 'business': business, 'posts':posts})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    hood = Hood.objects.all()

    return render(request, 'profile.html', {'profile': profile, 'hood':hood})


@login_required(login_url='/accounts/login/')
def hood(request, hood_id):

    return render(request, 'hood.html')


@login_required(login_url='/accounts/login/')
def business(request, hood_id):
    try:
        business = Business.objects.get(id=hood_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "business.html", {"business": business})


@login_required(login_url='/accounts/login/')
def location(request, location_id):

    return render(request, 'location.html')


@login_required(login_url='/accounts/login/')
def contact(request):

    return render(request, 'contact.html')


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_business_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
