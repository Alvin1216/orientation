from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.models import User, UserInfo
from django.http import JsonResponse


# Create your views here.

def hello_world(request):
    return HttpResponse("HelloWorld!")


def index(request):
    name = "Pika~"
    current_time = str(datetime.now())
    return render(request, 'myapp/index.html', locals())


# locals是拿來傳參數

def tag_page(request):
    animals = ['cat', 'dog', 'pikachu']
    return render(request, 'myapp/tag.html', locals())


def create_user(request):
    u = User.objects.create(name='alvin')
    u.save()
    ui = UserInfo.objects.create(user_id=u, age=23)
    ui.save()
    return JsonResponse({'state': 'success'})


def get_user_list(request):
    # find all the people
    U = User.objects.all()

    # only find the name is lisa
    # U = User.objects.filter(name=“lisa”)

    # take the data from U(Object that contained all the people)
    nameList = []
    for user in U:
        nameList.append(user.name)
    return JsonResponse({'userList': nameList})


def get_user_agelist(request):
    # only find the name is lisa
    U = User.objects.filter(name='lisa')
    print(U)
    ageList = []
    for user in U:
        print(user.name)
        age = UserInfo.objects.filter(user_id=user)[0]
        print(age.age)
        ageList.append(age.age)
    return JsonResponse({'ageList': ageList})
