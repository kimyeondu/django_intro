from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
from datetime import datetime

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    # return HttpResponse('Welcome to Django !!')
    return render(request, 'index.html')

def dinner(request):
    menus = ['양배추', '브로콜리', '오이', '딸기', '당근']
    pick = random.choice(menus)
    # return HttpResponse(pick)
    return render(request, 'dinner.html', {'menus':menus, 'pick':pick})
    
def hello(request, name):

    return render(request, 'hello.html', {'name':name})

def cube(request, num):
    cubes = num**3
    return render(request, 'cube.html', {'num':num, 'cubes':cubes})

# get 형식
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    # dict 형식이기 때문에 get
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data':data})

# post 형식
def user_new(request):

    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    return render(request, 'user_create.html', {'nickname':nickname, 'password':password})

def template_example(request):
    my_list = ['짜장면', '탕수육', '짬뽕', '양장피', '사과맛쿠키']
    my_sentence = 'Life if short, you need Python'
    messages = ['apple', 'banana', 'strawberry', 'watermelon', '냠냠']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'template_example.html',
                    {'my_list':my_list, 'my_sentence':my_sentence,
                    'messages':messages, 'empty_list': empty_list, 'datetimenow':datetimenow})

def static_example(request):
    return render(request, 'static_example.html')