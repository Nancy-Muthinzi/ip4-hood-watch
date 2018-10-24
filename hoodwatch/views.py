from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
import datetime as dt
from .models import Hood, Profile, Business, Post
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    business = Business.objects.all()

    business = Business.objects.all()
    profiles = Profile.objects.all()
    posts = Post.objects.all()
    hoods = Hood.objects.all()

    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'home.html', {'date': date, 'hood':hoods, 'profile':profiles, 'postForm': form, 'business': business, 'post':posts})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    hood = Hood.objects.all()

    return render(request, 'profile.html', {'profile': profile, 'hood':hood})


@login_required(login_url='/accounts/login/')
def hood(request, hood_id):
    postform = PostForm()
    hood_it = get_object_or_404(Hood,pk=hood_id)
    business = Business.objects.filter(hood=hood_it)
    # print(hood_it)
    # print('ppppppppppp')
    that_hood=Post.objects.filter(hood=hood_it)
    return render(request, 'hood.html',locals())

@login_required(login_url='/accounts/login/')
def new_hood(request, hood_id):
    current_user = request.user

    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.profile = current_user
            hood.save()
        return redirect('home')

    else:
        nform = NewHoodForm()

    return render(request, 'new_hood.html', {"form": nform})

@login_required(login_url='/accounts/login/')
def business(request, hood_id):
    try:
        business = Business.objects.get(id=hood_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "business.html", {"business": business})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.user

    if request.method == 'POST':
        form = NewBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = current_user
            business.save()
        return redirect('home')

    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form": form})

def post(request, post_id):
    post = get_object_or_404(Image, pk=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.image = post
            post.save()
    return redirect('home')

    return render(request, 'home.html')

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
