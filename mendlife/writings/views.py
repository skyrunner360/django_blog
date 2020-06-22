from django.shortcuts import render
from .models import Writing

# Create your views here.
def wHome(request):
    allwriting = Writing.objects.all()
    context = {'writing': allwriting}
    return render(request,'writings/wHome.html', context)
def wPost(request,slug):
    w = Writing.objects.filter(slug=slug).first()
    context = {'writings': w}
    return render(request,'writings/wPost.html', context)