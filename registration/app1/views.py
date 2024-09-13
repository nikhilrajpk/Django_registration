from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages
# Create your views here.

# @login_required(login_url='login')
@never_cache
def homePage(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    return redirect(LoginPage)

@never_cache
def signupPage(request):
    pass_validate = ""
    if request.user.is_authenticated:
        return redirect(homePage)
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 != pass2:
            pass_validate = "password does not match!"
            return render(request,'signup.html',{'pass_validate':pass_validate})
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect(LoginPage)
    else:
        return render(request,'signup.html')

@never_cache
def LoginPage(request):
    result = ""
    if request.user.is_authenticated:
        return redirect(homePage)
    if request.method == 'POST':
        username = request.POST.get('username')        
        pass1 = request.POST.get('pass')
        user = authenticate(request,username = username,password = pass1)
        
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect(adminPage)
            else:
                return redirect(homePage)
        else:
            result = "username or password is incorrect!"
            return render(request,'login.html',{'result':result})
    else:
        return render(request,'login.html')

@never_cache
def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(LoginPage)

@never_cache
def adminPage(request):
    if request.user.is_authenticated:
        user_obj = User.objects.all().filter(is_staff = False)
        context = {'user_obj' : user_obj}
        # print(user_obj.values())
        return render(request,'adminPage.html',context)
    else:
        return redirect(signupPage)
@never_cache
def create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email') 
        password = request.POST.get('password')
        
        user_obj = User.objects.create_user(username, email, password)
        print(user_obj)
        user_obj.save()
        
        return redirect(adminPage)  

@never_cache
def edit(request):
    if request.user.is_authenticated:
        user_obj = User.objects.all().filter(is_staff = False)
        context = { 'user_obj' : user_obj }
        return redirect(request,'adminPage.html',context)
    else:
        return redirect(LoginPage)
    
@never_cache
def update(request,id):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        user_obj = User(
            id = id,
            username = username,
            email = email
        )
        user_obj.save()
    return redirect(adminPage)

@never_cache
def delete(request,id):
    if request.method == 'POST':    
        user_obj = User.objects.filter(id = id)
        user_obj.delete()
        return redirect(adminPage)
    else:
        return redirect(adminPage)