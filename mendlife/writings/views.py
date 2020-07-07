from django.shortcuts import render,redirect
from .models import Writing, WComment
from django.contrib import messages
from writings.templatetags import extras

# Create your views here.
def wHome(request):
    allwriting = Writing.objects.all()
    context = {'writing': allwriting}
    return render(request,'writings/wHome.html', context)
def wPost(request,slug):
    w = Writing.objects.filter(slug=slug).first()
    w.views = w.views+1
    w.save()
    comments = WComment.objects.filter(wpost=w, parent=None)
    replies = WComment.objects.filter(wpost=w).exclude(parent=None)
    #Creating Reply Dictionary and iterating it 
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'writings': w,'comments': comments,'user' : request.user,'replyDict' : replyDict}
    return render(request,'writings/wPost.html', context)
def postComment(request):
    if request.method=="POST":
        comment = request.POST.get("comment")
        user = request.user
        wSno = request.POST.get("wSno") 
        post = Writing.objects.get(sno=wSno)
        #Posting Replies
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = WComment(comment=comment,user=user, wpost=post)
            comment.save()
            messages.success(request,"Your Comment has been posted successfully")
        else:
            parent = WComment.objects.get(sno=parentSno)
            comment = WComment(comment=comment,user=user,wpost=post, parent = parent)
            comment.save()
            messages.success(request,"Your Reply has been posted successfully")
        return redirect (f"/writings/{post.slug}")