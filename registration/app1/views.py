from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
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


def user_list(request):
    return render(request,'user_list.html')

def user_create(request):
    return render(request,'user_form.html')

def user_update(request):
    return render(request,'user_form.html')

def user_delete(request):
    return render(request,'user_confirm_delete')
