from django.shortcuts import render
from .models import Slideshow, Teams

# Create your views here.
def index(request):
    slide_images = Slideshow.objects.all()
    return render(request,'index.html',{"slide_images":slide_images})

def about(request):
    members = Teams.objects.all()
    return render(request,'about.html',{"members": members})

def resources(request):
    return render(request,'docindex.html')

def contact(request):
    return render(request,'contact.html')