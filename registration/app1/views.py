from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
# Create your views here.
def homePage(request):
    return render(request,'home.html')

def signupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        return HttpResponse("user has been created successfully !!!")
        print(uname,email,pass1,pass2)
        
    return render(request,'signup.html')

def LoginPage(request):
    return render(request,'login.html')