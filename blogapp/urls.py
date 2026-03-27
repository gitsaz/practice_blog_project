from django.urls import path

from .views import(
    home,
    blogs,
    blog_details,
    tag_blogs,
    category_blogs
)
urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blogs, name="blogs"),
    path('blog_details/<str:slug>/', blog_details, name="blog_details"),
    path('tag_blogs/<str:slug>/', tag_blogs, name="tag_blogs"),
    path('category_blogs/<str:slug>/', category_blogs, name="category_blogs")
]