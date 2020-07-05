from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post,Tech, BlogComment
from django.contrib import messages
from blog.templatetags import extras

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
    post.views = post.views+1
    post.save() 
    tech = Tech.objects.filter(slug=slug).first()
    tech.views = tech.views+1
    tech.save()
    pcomments = BlogComment.objects.filter(post=post,parent=None)
    preplies = BlogComment.objects.filter(post=post).exclude(parent=None)
    #Creating Reply Dictionary and iterating it 
    preplyDict = {}
    for reply in preplies:
        if reply.parent.sno not in preplyDict.keys():
            preplyDict[reply.parent.sno] = [reply]
        else:
            preplyDict[reply.parent.sno].append(reply)
    tcomments = BlogComment.objects.filter(tech=tech,parent=None)
    treplies = BlogComment.objects.filter(tech=tech).exclude(parent=None)
    #Creating Reply Dictionary and iterating it 
    treplyDict = {}
    for reply in treplies:
        if reply.parent.sno not in treplyDict.keys():
            treplyDict[reply.parent.sno] = [reply]
        else:
            treplyDict[reply.parent.sno].append(reply)
    context = {'post': post,'tech':tech,'pcomments':pcomments,'tcomments':tcomments,'preplyDict':preplyDict,'treplyDict':treplyDict}
    return render(request,'blog/blogPost.html',context)
# The below function takes slug as another argument and passes it to blogpost like the commented line shown below
    # return HttpResponse(f'This is Blogpost: {slug}')
def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        parentSno = request.POST.get("parentSno")
        if request.POST.get("postSno"):
            postSno = request.POST.get("postSno") 
            post = Post.objects.get(sno=postSno)

            if parentSno == "":
                comment = BlogComment(comment=comment,user=user, post=post)
                comment.save()
                messages.success(request,"Your Comment has been posted successfully")
            else:
                parent = BlogComment.objects.get(sno=parentSno)
                comment = BlogComment(comment=comment,user=user, post=post, parent = parent)
                comment.save()
                messages.success(request,"Your Reply has been posted successfully")
            return redirect(f"/blog/{post.slug}")
        else:
            techSno = request.POST.get("techSno") 
            tech = Tech.objects.get(sno=techSno)
            if parentSno == "":
                comment = BlogComment(comment=comment,user=user, tech=tech)
                comment.save()
                messages.success(request,"Your Comment has been posted successfully")
            else:
                parent = BlogComment.objects.get(sno=parentSno)
                comment = BlogComment(comment=comment,user=user,tech=tech, parent = parent)
                comment.save()
                messages.success(request,"Your Reply has been posted successfully")
            return redirect(f"/blog/{tech.slug}")