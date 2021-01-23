from django.shortcuts import render

# Create your views here.

def seehome(request):
    return render(request,'home.html')

def seemap(request):
    return render(request, 'mappy.html')
