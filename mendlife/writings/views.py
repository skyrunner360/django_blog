from django.shortcuts import render,redirect
from .models import Writing, WComment
from django.contrib import messages

# Create your views here.
def wHome(request):
    allwriting = Writing.objects.all()
    context = {'writing': allwriting}
    return render(request,'writings/wHome.html', context)
def wPost(request,slug):
    w = Writing.objects.filter(slug=slug).first()
    comments = WComment.objects.filter(wpost=w)
    context = {'writings': w,'comments': comments}
    return render(request,'writings/wPost.html', context)
def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        wSno = request.POST.get("wSno") 
        post = Writing.objects.get(sno=wSno)
        comment = WComment(comment=comment,user=user,wpost=post)
        comment.save()
        messages.success(request,"Your Comment has been posted successfully")
        return redirect (f"/writings/{post.slug}")