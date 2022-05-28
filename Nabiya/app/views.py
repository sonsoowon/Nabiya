from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

@login_required(login_url='register/login')
def home(request):
    pass

def new_post_0(request):
    if request.method == "POST" :
        emotion = request.POST["emotion"]
        new_post = Diary.objects.create(writer=request.user, emotion=emotion, pet=request.pet)
        return redirect("new_post_1", new_post.pk)
    return render(request, 'new_post_0.html')

def new_post_1(request, post_pk):
    if request.method == "POST" :
        photo = request.POST["photo"]
        new_post = Diary.objects.filter(pk=post_pk).update(photo=photo)
        return redirect("new_post_2", new_post.pk)
    return render(request, "new_post_1.html")

def new_post_2(request, post_pk):
    if request.method == "POST" :
        content = request.POST["content"]
        new_post = Diary.objects.filter(pk=post_pk).update(content=content)
        return redirect("new_post_2", new_post.pk)
    return render(request, "new_post_2.html")

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

def login(request):
    pass

def signup(request):
    pass

def logout(request):
    pass