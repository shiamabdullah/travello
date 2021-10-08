from django.http import response
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if (request.method=='POST'):
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        password= request.POST['last_name']
        password2= request.POST['password2']
        email= request.POST['email']
        if (password==password2):
            if(User.objects.filter(username=username).exists()):
                user= User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
            else:
                print('username already exists')
        else:
            print('password not matching')
        
        return redirect('/')

    else:
        return render(request,'register.html')
