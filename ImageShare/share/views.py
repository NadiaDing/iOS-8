from django.shortcuts import render,redirect
from models import SharedImage
# Create your views here.

def upload(request):
    images = SharedImage.objects.all()
    return render(request, 'index.html',{'images':images})

def hnd_load(request):
    shr = SharedImage()
    shr.image = request.FILES['file']
    shr.title = request.POST['title']
    shr.description = request.POST['description']
    shr.save()
    return redirect('main')
