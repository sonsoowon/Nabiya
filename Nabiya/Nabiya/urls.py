"""Nabiya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'), # 첫 달력화면
    path('list/', views.list, name='list'),
    path('new_post/', views.new_post_1, name='new_post_1'),
    path('new_post/<int:post_pk>', views.new_post_2, name='new_post_2'),

    path('detail_post/<int:post_pk>', views.detail_post, name='detail_post'),
    
    path('mypage', views.mypage, name='mypage'), # home 화면 오른쪽 상단 아이콘 클릭 시 연결
    
    path('mypage/following', views.list_following, name='list_following'), # 내가 팔로우하는 사용자 목록
    path('mypage/follower', views.list_follower, name='list_follower'), # 나를 팔로우하는 사용자 목록
    path('follow/<int:user_pk>', views.follow, name='follow'), # 다른 사용자 팔로우 버튼 클릭 시 연결

    path('my_post', views.my_post, name='my_post'), # 내가 쓴 일기 목록

    # 검색 아이콘 클릭 시 연결
    path('search_user', views.search_user, name='search_user'),
    path('registration/login', views.login, name='login'), 
    path('registration/signup', views.signup, name='signup'), # 로그인 화면에서 가입하기 버튼 클릭 시 연결
    path('registration/logout', views.logout, name='logout'),
    path("accounts/", include("allauth.urls")),
   


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
