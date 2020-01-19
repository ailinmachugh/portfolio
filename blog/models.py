from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField( max_length=20)

class Post(models.Model):
    title = models.CharField( max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField( auto_now=True)
    last_modified = models.DateField( auto_now=True )
    caegories = models.ManyToManyField('Category', related_name ='post')

class Comment(models.Model):
    author = models.CharField( max_length=50)
    body = models.TextField()
    created_on = models.DateField( auto_now=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)