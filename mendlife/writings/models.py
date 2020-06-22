from django.db import models

# Create your models here.
#Creating a Blog class for life update blogs
class Writing(models.Model):
    sno= models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=13)
    author = models.CharField(max_length=100)
    slug = models.CharField(max_length=150,default=" ")
    timeStamp = models.DateTimeField(blank=True)
    img = models.ImageField(upload_to="writings/", blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author