from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Class_name

def index(request):
    posts = Class_name.objects.all()
    paginator = Paginator(posts,3) 
    now_page = request.GET.get('page')
    posts = paginator.get_page(now_page) 
    context= {
        "posts":posts
    }    

    return render(request,'index.html',context)

def read(request,post_id):
    post = Class_name.objects.get(id=post_id)
    context = {
        "post":post
    }

    return render(request,'read.html',context)

def create(request): 
    if request.method == "GET":
        return render(request,'create.html')

    elif request.method == "POST":
        post = Class_name()

        post.user = request.user

        post.table_name1 = request.POST['post.table_name1']
        post.table_name2 = request.POST['post.table_name2'] 
        post.category = request.POST['category']
        
        try:
            post.pic = request.FILES['pic']
        except:
            pass
        post.save()

        return redirect(index)

def update(request,post_id):
    if request.method == "GET":
        post = Class_name.objects.get(id=post_id)
        context={
            "post":post
        }
        return render(request,'update.html',context)
    
    elif request.method == "POST":
        post = Class_name.objects.get(id=post_id)
        post.table_name1 = request.POST['post.table_name1']
        post.table_name2 = request.POST['post.table_name2']
        post.save()
        return redirect(index)

def delete(request,post_id):
    post = Class_name.objects.get(id=post_id)
    post.delete()
    return redirect(index)

def search(request):
    search_text = request.GET['search']
    search_filter = request.GET['search_filter']
    if search_filter == "제목":
        posts = Class_name.objects.filter(table_name1__icontains=search_text)
    elif search_filter == "내용":
        posts = Class_name.objects.filter(table_name2__icontains=search_text)
    elif search_filter == "제목+내용":
        posts = Class_name.objects.filter(Q(table_name1__icontains=search_text)|Q(table_name2__icontains=search_text))
    context={
        "posts":posts
    }
    return render(request,'search.html',context)

def category(request):
    search_category = request.GET['category']
    posts = Class_name.objects.filter(category=search_category)
    context={
        "posts":posts
    }
    return render(request,'category.html',context)