from django.shortcuts import render, get_object_or_404
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
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
    queryset = Blog.objects.order_by('-created_date')
    tags = Tag.objects.order_by('-created_date')
    categories = Category.objects.order_by('-created_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 2)
    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(1)
        
        
    context = {
        'blogs':blogs,
        'tags':tags,
        'categories':categories,
        'paginator':paginator
    }
    
    return render(request, 'blogs.html', context)


def PostDetails(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    context = {
        'blog':blog
    }
    
    return render(request, 'post_details.html', context)


def tag_blogs(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    tags = Tag.objects.order_by('-created_date')
    blogs = tag.tag_blogs.all()
    categories = Category.objects.all()
    
    context = {
        'tags':tags,
        'blogs':blogs,
        'categories':categories
    }
    
    return render(request, 'tag_blogs.html', context)



def category_blogs(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.order_by('-created_date')
    blogs = category.category_blogs.all()
    tags = Tag.objects.all()
    
    context = {
        'tags':tags,
        'blogs':blogs,
        'categories':categories
    }
    
    return render(request, 'category_blogs.html', context)