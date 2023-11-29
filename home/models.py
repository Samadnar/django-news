from .manager import BaseModel
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
            return self.name
        
class Tags(BaseModel):
    name = models.CharField(max_length=255)
    def __str__(self) -> str:
            return self.name

class  News(BaseModel):
    title = models.CharField(max_length = 255)
    img = models.ImageField(upload_to='news/')
    body = RichTextField()
    slug = models.SlugField()
    view_count = models.BigIntegerField(default=0, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True, related_name='category_news' )
    tags = models.ManyToManyField(Tags, related_name='tag_news' )
    
    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self) -> str:
        return self.name    
