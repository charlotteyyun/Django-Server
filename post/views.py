from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context ={}
    return render(request, 'post/index.html', context)

def art(request):
    context ={}
    return render(request, 'post/art.html', context)

def physics(request):
    context ={}
    return render(request, 'post/physics.html', context)

def dance(request):
    context ={}
    return render(request, 'post/dance.html', context)