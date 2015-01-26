from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle
from django.contrib.auth import authenticate, login

# Create your views here.
user=""

def index(request):
    blogs=BlogArticle.objects.all()
    if request.method =="POST":
        usname=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(username=usname,password=pwd)
        if user is not None:
            login(request,user)
            return render(request, "main.html",{'testvar':"Test String 2!","blogs":blogs,'user':user})
    return render(request,"main.html",{'testvar':"Test String 2!","blogs":blogs,'user':None})


def createBlog(request):
    newBlog=BlogArticle()
    newBlog.title=request.POST['title']
    newBlog.author=request.user
    newBlog.blog_content=request.POST['blog_content']
    newBlog.save()
    blogs=BlogArticle.objects.all()
    return render(request, "main.html",{'testvar':"Test String 2!","blogs":blogs,'user':user})
