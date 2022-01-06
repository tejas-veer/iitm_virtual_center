from django.shortcuts import render
from .models import slideshow

# Create your views here.
def index(request):
    slides_img = slideshow.objects.all()
    return render(request,'index.html',{"slide_images":slides_img})

def about(request):
    slides_img = slideshow.objects.all()
    return render(request,'about.html',{"slide_images":slides_img})

def resources(request):
    slides_img = slideshow.objects.all()
    return render(request,'courses.html',{"slide_images":slides_img})

def contact(request):
    slides_img = slideshow.objects.all()
    return render(request,'contact.html',{"slide_images":slides_img})