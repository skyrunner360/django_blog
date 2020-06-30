from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Post, Tech
from writings.models import Writing
from itertools import chain
from django.db.models import Q


# Create your views here.
# HTML Pages
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
# Authentication APIs
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
        #Username should be under 15 Characters
        if len(username) > 15:
            messages.error(request,"Your Username must be under 15 characters ")
            return redirect('home')
        #Username should be alphanumeric
        if not username.isalnum() :
            messages.error(request,"Username Should only contain letters and numbers")
            return redirect('home')
        #Both Passwords should match
        if pass1 != pass2:
            messages.error(request,"Passwords Do not Match")
            return redirect('home')
        #Create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Account has been Successfully created")
        return redirect('home')

    else:
        return HttpResponse('404- Not Found')
def handleLogin(request):
    if request.method == 'POST':
        #Get the Post Parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials, Please try again")
            return redirect('home')

    return HttpResponse('404- Not Found')
def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out!")
    return redirect('home')
