from django.urls import path

from .views import(
    home,
    blogs,
    PostDetails
)
urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blogs, name="blogs"),
    path('post_details/<slug:slug>/', PostDetails, name="post_details")
]