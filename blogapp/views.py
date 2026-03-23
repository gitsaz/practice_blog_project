from django.shortcuts import render
from .models import Blog, Category, Tag

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    categories =Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'blogs':blogs,
        'categories':categories,
        'tags':tags
    }
    return render(request, 'home.html', context)

def blogs(request):
    return render(request, 'blogs.html')