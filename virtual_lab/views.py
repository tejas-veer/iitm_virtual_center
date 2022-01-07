from django.shortcuts import render
from .models import slideshow

# Create your views here.
def index(request):
    slides_img = slideshow.objects.all()
    return render(request,'index.html',{"slide_images":slides_img})

def about(request):
    slides_img = slideshow.objects.all()
    return render(request,'about.html',)

def resources(request):
    slides_img = slideshow.objects.all()
    return render(request,'courses.html')

def contact(request):
    slides_img = slideshow.objects.all()
    return render(request,'contact.html')