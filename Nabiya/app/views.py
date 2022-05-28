from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core import serializers

from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def start(request):
    return render(request, 'start.html')

@login_required(login_url='register/login')
def home(request):
    diarys = serializers.serialize("json", Diary.objects.all())
    return render(request, 'home.html', {'diarys':diarys})


def new_post_1(request):
    if request.method == "POST" :
        photo = request.POST["photo"]
        new_post = Diary.objects.create(photo=photo)
        return redirect("new_post_2", new_post.pk)
    return render(request, "new_post_1.html")

def new_post_2(request, post_pk):
    if request.method == "POST" :
        emotion = request.POST["emotion"]
        content = request.POST["content"]
        new_post = Diary.objects.filter(pk=post_pk).update(content=content, emotion=emotion)
        return redirect("detail", new_post.pk)
    return render(request, "new_post_2.html")

def detail_post(request, post_pk):
    post = Diary.objects.get(pk=post_pk)
    return render(request, "detail.html", {"post": post})


def add_pet(request):
    if request.method == "POST":
        add_pet = Pet.objects.create(
            profile_img = request.POST["profile_img"],
            name = request.POST["name"],
            birth = request.POST["birth"],
            introduction = request.POST["introduction"],
            species = request.POST["species"]
        )
        return redirect("home")
    return render(request, "add_pet.html")


def add_another_pet(request):
    if request.method == "POST":
        add_pet = Pet.objects.create(
            profile_img = request.POST["profile_img"],
            name = request.POST["name"],
            birth = request.POST["birth"],
            introduction = request.POST["introduction"],
            species = request.POST["species"]
        )
        return redirect("home")
    return render(request, "home.html")

@login_required(login_url='register/login')
def mypage(request):
    pass


def list_following(request):
    pass

def list_follower(reqeust):
    pass

@login_required(login_url='register/login')
def follow(request, user_pk):
    pass


def my_post(request):
    pass

# 검색어 입력 전에 게시물 나열
# 검색어 입력 시 실시간 필터링 적용(JS)
def search_user(request):
    pass
        

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
            # return redirect(request.GET.get("next","/"))
            return redirect("home")
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, "registration/login.html", {"error":error})

    return render(request, "registration/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        found_user = User.objects.filter(username=username)
        if len(found_user):
            error = "이미 존재하는 아이디입니다"
            return render(request,"registration/signup.html", {"error":error})
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)
        return redirect("home")
    return render(request, "registration/signup.html")

def logout(request):
    auth.logout(request)

    return redirect("start")