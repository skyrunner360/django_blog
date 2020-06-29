from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from blog.models import Post, Tech
from writings.models import Writing
from itertools import chain
from django.db.models import Q


# Create your views here.
def home(request):
    #get all posts from blog model
    allpost = Writing.objects.all()
    #Send all posts as dictionary in the render function
    sending = {'writing' : allpost}
    # This function return's home.html file from templates/home folder
    return render(request,'home/home.html',sending)
def contact(request):
    #Get values from contact form and save them to database
    if request.method=='POST':
        #Getting Values
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        #Check for Valid Form Entries
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"Please Fill the form Correctly")
        else:
        #Make Contact object of model and save it
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            #Display a Success Message on form submition
            messages.success(request,'Your message has been sent')

    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')
def search(request):
    query = request.GET['query']
    if len(query)>100:
        allpost= Writing.objects.none()
    else:
        w = Writing.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        p = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        t = Tech.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        allpost = list(chain(w,p,t))
    # if allpost.count() == 0:
    #     messages.warning(request,"No search results found please refine your query")
    params = {'allpost': allpost,'query':query}
    return render(request,'home/search.html',params)
def handleSignup(request):
    if request.method == 'POST':
        #Get the Post Parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Check for errorneous inputs
        #

        #Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Account has been Successfully created")
        
    else:
        return HttpResponse('404- Not Found')
