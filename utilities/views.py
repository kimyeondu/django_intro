from django.shortcuts import render

# Create your views here. utilities view!

def index(request):
    return render(request, 'utilities/index.html')
