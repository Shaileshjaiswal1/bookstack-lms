from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import AddBook
from lms_app.models import AddBook
from api.serializers import BookSerializers
from django.urls import reverse


# Create your views here.
def signup(request):  
    if request.method == "GET":
        return render(request, 'admin/signup.html')
    else:
        context = {}
        adminMail = request.POST.get('email')
        adminPass = request.POST.get('password')

        print("Admin Email:", adminMail)
        print("Admin Password:", adminPass)

        if adminMail == '' or adminPass == '':
            context['errorMsg'] = "Field Can not be Empty"
        elif len(adminPass)<8:
            context['errorMsg'] = 'Password must be at least 8 characters long.'
        elif User.objects.filter(email=adminMail).exists():
            context['errorMsg'] = 'Email is already registered. Please log in.'
        else:            
            try:
                signupQuery = User.objects.create_user(username=adminMail, email=adminMail, password=adminPass)
                signupQuery.set_password(adminPass)
                signupQuery.save()
                context['success'] = 'User Registered Successfully..!'
            except Exception:
                context['errorMsg'] = 'Account already exists. Please log in.'

        return render(request, 'admin/signup.html', context)


def adminlogin(request):
    if request.method == 'GET':
        return render(request,'admin/adminlogin.html')
    else:
        context = {}
        adminMail = request.POST.get('email')
        adminPass = request.POST.get('password')

        adminAuthentication = authenticate(username=adminMail,password=adminPass)

        if adminMail == '' or adminPass == '':
            context['errorMsg'] = 'Email and password are required. Please fill in both fields.'
            return render(request,'admin/adminlogin.html',context)
        elif adminAuthentication == None:
            context['errorMsg'] = 'Invalid credentials. Please try again.'
            return render(request,'admin/adminlogin.html',context)
        else:
            login(request,adminAuthentication)
            return redirect(reverse('dashboard'))
        
def base(request):
    books = AddBook.objects.all()
    serializer = BookSerializers(books, many=True)
    return render(request, 'student/base.html', {'books': serializer.data})


    