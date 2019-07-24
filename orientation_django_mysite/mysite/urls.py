"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myapp import views
#from package import module
#下面用的名字就是這個modele的檔名
#這個例子就是myapp這個package，裡面的views.py這個module
#想用views.py之中的函式hello_world
#直接views.hello_world就好
import orientation.views as orientation_view
#import 某個package中(也就是某個檔案夾中，檔案夾中要有_init.py，才可以這樣做)
#，裡面某一個module(也就是裡面某個.py檔，而這個.py檔中有很多個函式可以調用)
#怕名字衝突，所以用as直接重新命名成orientation_view
#import package.module as <new_name>

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world),
    path('', views.index),
    path('tag/', views.tag_page),
    path("createUser/", views.createUser),
    path("getUser/", views.getUser),
    path("getAge/", views.getAge),
    path("getType/",orientation_view.return_song_with_type),
    path("insert/",orientation_view.insert_song),
    path("delete/",orientation_view.delete_song),
    path("modified/",orientation_view.modified_song),
    path("search/",orientation_view.search_song),
]
