from django.urls import path

from .views import(
    home,
    blogs,
    blog_details,
    tag_blogs,
    category_blogs,
    about,
    reply,
    search_blog,
    user_profile
)
urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blogs, name="blogs"),
    path('blog_details/<str:slug>/', blog_details, name="blog_details"),
    path('tag_blogs/<str:slug>/', tag_blogs, name="tag_blogs"),
    path('category_blogs/<str:slug>/', category_blogs, name="category_blogs"),
    path("reply/<int:blog_id>/<int:comment_id>/", reply, name="reply"),
    path('search_blog/', search_blog, name="search_blog"),
    path('user_profile/', user_profile, name="user_profile"),
    path('about/', about, name="about")
]