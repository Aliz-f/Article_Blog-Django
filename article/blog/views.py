from django.shortcuts import render
from django.http import HttpResponse

posts = [

    {
        'author': 'Alirzea',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Feb 13, 2021'
    },
    {
        'author': 'Mohammad',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'Feb 14, 2021'
    }

]

def home (request):
    
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about (request):
    return render(request, 'blog/about.html', {'title' : 'About'})
    