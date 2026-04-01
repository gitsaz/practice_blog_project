from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .models import Blog, Category, Tag, Comment, Reply
from .forms import TextForm

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


def blog_details(request, slug):
    form = TextForm()
    blog = get_object_or_404(Blog, slug=slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    related_post = Blog.objects.filter(category=blog.category).exclude(id=blog.id).order_by('-id')
    
    if not related_post:
        related_post = Blog.objects.filter(category=blog.category).exclude(id=blog.id).order_by('-created_date')
        
    if request.method == 'POST' and request.user.is_authenticated:
        form = TextForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                user=request.user,
                blog=blog,
                text=form.cleaned_data.get('text') 
            )
            return redirect('blog_details', slug=slug)
    
    context = {
        'blog':blog,
        'categories':categories,
        'tags':tags,
        'related_post':related_post,
        'form':form
    }
    
    return render(request, 'blog_details.html', context)


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



@login_required(login_url="")
def reply(request, blog_id, comment_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = TextForm(request.POST)
        if form.is_valid():
            comment = get_object_or_404(Comment, id=comment_id)
            Reply.objects.create(
            user = request.user,
            comment = comment,
            text = form.cleaned_data.get("text")
            )
    return redirect("blog_details", slug=blog.slug)

def search_blog(request):
    search_key = request.GET.get('search', None)
    tags = Tag.objects.all()
    categories = Category.objects.all() 
    
    if search_key:
        blogs = Blog.objects.filter(
            Q(title__icontains=search_key) |
            Q(category__title__icontains=search_key) |
            Q(tag__title__icontains=search_key) |
            Q(user__username__icontains=search_key)
        ).distinct
    
        context = {
            "blogs":blogs,
            "tags":tags,
            "categories":categories
        }
        return render(request, "search_blog.html", context)   

    else:
        blogs = Blog.objects.all()
        context = {
            "blogs":blogs
        }
        return render(request, "search_blog.html", context)
        
        
def about(request):
    return render(request, 'about.html')