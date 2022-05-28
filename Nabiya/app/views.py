import re
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required(login_url='register/login')
def home(request):
    pass



def new_post_2(request):
    if request.method == "POST" :
        emotion = request.POST["emotion"]
        content = request.POST["content"]
        photo = request.FILES.get("photo")
        new_post = Diary.objects.create(content=content, emotion=emotion, photo=photo)
        return redirect("detail_post", new_post.pk)
    return render(request, "new_post_2.html")

def detail_post(request, post_pk):
    post = Diary.objects.get(pk=post_pk)
    return render(request, "detail_post.html", {"post": post})


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

def list(request):
    posts = Diary.objects.all()
    return render(request, "list.html", {"posts": posts})


def my_post(request):
    pass

# 검색어 입력 전에 게시물 나열
# 검색어 입력 시 실시간 필터링 적용(JS)
def search_user(request):
    pass

def login(request):
    pass

def signup(request):
    pass

def logout(request):
    pass