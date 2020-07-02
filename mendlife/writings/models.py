from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

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

class WComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wpost = models.ForeignKey(Writing, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + " ... " + "by " + self.user.username