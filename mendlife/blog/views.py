from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post,Tech, BlogComment
from django.contrib import messages

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
    pcomments = BlogComment.objects.filter(post=post)
    tcomments = BlogComment.objects.filter(post=tech)
    context = {'post': post,'tech':tech,'pcomments':pcomments,'tcomments':tcomments}
    return render(request,'blog/blogPost.html',context)
# The below function takes slug as another argument and passes it to blogpost like the commented line shown below
    # return HttpResponse(f'This is Blogpost: {slug}')
def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno") 
        post = Post.objects.get(sno=postSno)

        comment = BlogComment(comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,"Your Comment has been posted successfully")
    return redirect("/blog/{post.slug}")