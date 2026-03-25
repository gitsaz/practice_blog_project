from django.urls import path

from .views import(
    home,
    blogs,
    PostDetails,
    tag_blogs,
    category_blogs
)
urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blogs, name="blogs"),
    path('post_details/<slug:slug>/', PostDetails, name="post_details"),
    path('tag_blogs/<str:slug>/', tag_blogs, name="tag_blogs"),
    path('category_blogs/<str:slug>/', category_blogs, name="category_blogs")
]