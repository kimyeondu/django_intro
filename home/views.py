from django.shortcuts import render, HttpResponse
from pprint import pprint
import random
# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django !!')

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