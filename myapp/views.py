from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


# Create your views here.

def signup_view(request):
    if request.method=="POST":
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
               return render(request, 'signup.html', {'error': 'Username already exists.'})
            else:
                data= User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                data.save()
                
                return redirect('login')
        else:
             return redirect(request,'signup.html')
    return render(request,'signup.html')

def login_view(request):
        if request.method=="POST":
            username=request.POST.get("Username")
            password=request.POST.get("Password")
            user=auth.authenticate(username=username,password=password )
            
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                return render(request,'login.html',{'error':'Invalid username or password'})
                
    
        return render(request,'login.html')




def index(request):
    return render(request,'index.html')