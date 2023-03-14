from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    img = models.ImageField(upload_to='static/images/')
    introce = models.CharField(max_length=155)
    content = models.TextField()
    contentend = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_posted']

class Contact(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)