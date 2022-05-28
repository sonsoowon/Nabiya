from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required(login_url='register/login')
def home(request):
    pass

def new_post(request):
    pass

def detail_post(request, post_pk):
    pass

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

# 로그인 로그아웃 회원가입
# 로그인 로그아웃 회원가입
# 로그인 로그아웃 회원가입

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
        return redirect("list_page")
    return render(request, "registration/signup.html")

def logout(request):
    auth.logout(request)

    return redirect("start")

# 로그인 로그아웃 회원가입
# 로그인 로그아웃 회원가입
# 로그인 로그아웃 회원가입