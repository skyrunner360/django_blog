from django.shortcuts import render, HttpResponse
from blog.models import Post,Tech

# Create your views here.
def blogHome(request):
    #get all posts from blog model
    allpost = Post.objects.all()
    tech = Tech.objects.all()
    #Send all posts as dictionary in the render function
    context = {'allPosts': allpost,'techblog': tech}
    return render(request,'blog/blogHome.html', context)
def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    tech = Tech.objects.filter(slug=slug).first()
    context = {'post': post,'tech':tech}
    return render(request,'blog/blogPost.html',context)
# The below function takes slug as another argument and passes it to blogpost like the commented line shown below
    # return HttpResponse(f'This is Blogpost: {slug}')