import os
from django.shortcuts import render
from datetime import datetime, timedelta
import requests
import json


# Create your views here. utilities view!
# 2/28, 5/28

def index(request):
    return render(request, 'utilities/index.html')

datetimenow = datetime.now()

def bye(request):

    byedate = datetime(2019, 2, 28)
    remaindate = datetimenow - byedate
    return render(request, 'utilities/bye.html', {'datetimenow':datetimenow, 'remaindate':remaindate, 'byedate':byedate})
    
def graduation(request):
    graddate = datetime(2019, 5, 28)
    remaindate2 = datetimenow - graddate
    return render(request, 'utilities/graduation.html', {'datetimenow':datetimenow, 'graddate':graddate, 'remaindate2':remaindate2})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=daejeon,kr&lang=kr&APPID='
    my_url = url + key
    req = requests.get(my_url).json()
    # jsonreq = req.json()
    temp_min = req['main']['temp_min'] - 273.15
    temp_max = req['main']['temp_max'] - 273.15
    weather = req['weather'][0]['description']

    return render(request, 'utilities/today.html', {"temp_max":temp_max,"temp_min":temp_min, 'weather':weather})
    
    
    
    
    
    
def ascii_new(request):

    return render(request, 'utilities/ascii_new.html')
    
def ascii_make(request):
    text = request.GET.get('text')
    font = request.GET.get('font')
    url = f'http://artii.herokuapp.com/make?text={text}&font={font}'
    req = requests.get(url).text
    return render(request, 'utilities/ascii_make.html', {'req':req})
    
def original(request):
    return render(request, 'utilities/original.html')
    
    
naver_client_id = os.getenv('NAVER_TOKEN')
naver_client_secret = os.getenv('NAVER_SECRET_TOKEN')

def translated(request):
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"
    
    
    headers = {
    "X-Naver-Client-Id": naver_client_id,
    "X-Naver-Client-Secret": naver_client_secret
    }
    
    text = request.GET.get('kor')
    
    data = {
        "source": "ko",
        "target": "en",
        "text": text
    }
    
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response["message"]["result"]["translatedText"]
    
    return render(request, 'utilities/translated.html', {'reply_text':reply_text})