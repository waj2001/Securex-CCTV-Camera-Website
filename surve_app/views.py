from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib import auth


# Create your views here.
def home(request):

    df = employee_db
    df1 = df.objects.all()

    obj = ourservices
    obj1 = obj.objects.all()

    return render(request,"index.html",{'data':df1,'ser':obj1})


def sign_in(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']

        user = auth.authenticate(username = Username,password = Password)

        if user is not None:
            auth.login(request,user)
            return redirect("signout")
        else:
            messages.info(request,"Incorrect credential, please try again")
            return redirect("signin")
    return render(request,"signin.html")

def sign_up(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        Username = request.POST['Username']
        Email = request.POST['Email']
        Password1 = request.POST['Password1']
        Password2 = request.POST['Password2']

        if Password1==Password2:
            if User.objects.filter(email=Email).exists():
                messages.info(request,"This email_id already used")
                return redirect("signup")
            
            elif User.objects.filter(username=Username).exists():
                messages.info(request,"This Username already used")
                return redirect("signup")
            
            else:
                user = User.objects.create_user(username=Username,password=Password1,email=Email,first_name=First_name,last_name=Last_name)
                user.save()
                return redirect("signin")
        else:
            messages.info(request,"didn't match both password")
            return redirect ("signup") 

    return render(request,"signup.html")

def sign_out(request):
    auth.logout(request)
    return redirect("/")

def calc(request):
    return render(request,"calc.html")

def add(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])

    add = num1+num2

    return render(request,"result.html",{'res':add})

def sub(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])

    sub = num1-num2

    return render(request,"result.html",{'res':sub})

def mult(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])

    mult = num1*num2

    return render(request,"result.html",{'res':mult})

def div(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])

    div = num1/num2

    return render(request,"result.html",{'res':div})

def appoin(request):
    if request.method == 'POST':
        name = request.POST['name']
        email= request.POST['email']
        mobile = request.POST['mobile']
        service = request.POST['service']
        descr = request.POST['descr']

        df1 = appointment.objects.create(name=name,email=email,mobile=mobile,services=service,description=descr)
        df1.save()
    else:
        return redirect("appointment")
    
    return redirect("appointment")