from django.shortcuts import render , redirect
from userauths.forms import UserRegistrationForm 
from django.contrib.auth import login, authenticate ,logout
from django.contrib import messages 
from django.conf import settings
from userauths.models import User
# User = settings.AUTH_USER_MODEL
# Create your views here.

def register_view(request):
    
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            message = messages.success(request,f"Hey {username} , your account created sucessfully")
            new_user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])

            login(request, new_user)
            return redirect('core:index')
        else:
            print("Form errors:", form.errors) 
    else :
        form = UserRegistrationForm()
    
    context = {
        'form':form,
        'error':form.errors
    }
    return render(request,'userauths/sign-up.html',context)



def login_view(request):

    if request.user.is_authenticated:
        messages.warning(request,f"Hey you are already login")
        
        return redirect('core:index')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        try:
            user = User.objects.get(email=email)
            
        except:
            messages.warning(request,f"User with {email} does not exist")

        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            
            login(request,user)
            messages.success(request,'You are logged in. ')
            
            return redirect('core:index')
        else :
        
            messages.warning(request,"User Does Not Exist. Create an account. ")
        

    context={
       
    }
   
    return render(request,'userauths/sign-in.html',context)
        

def logout_view(request):
    logout(request)
    messages.success(request,'You logged out')
    return redirect("userauths:signup")