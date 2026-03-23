from django.db import models
from django.utils.text import slugify
from account.models import User
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    
class Tag(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    
class Blog(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_blogs',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        related_name='category_blogs',
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(
        Tag,
        related_name='tag_blogs',
        blank=True
    )
    title = models.CharField(
        max_length=250,
    )
    description = models.TextField(
        max_length=1000,
    )
    slug = models.SlugField(blank=True, unique=True)
    banner = models.ImageField(upload_to='blogs_banner')
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
    
class Comment(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_comment',
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        Blog,
        related_name='blogs_comment',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
class Reply(models.Model):
    user = models.ForeignKey(
        User,
        related_name='user_reply',
        on_delete=models.CASCADE
    )
    comment = models.ForeignKey(
        Comment,
        related_name='comment_reply',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.text