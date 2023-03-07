from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import client
# Create your views here.


def index(request):
    if request.method =='POST':
        usename =request.POST['username']
        password =request.POST['password']
        
        user = auth.authenticate(username=usename,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect(form)
        else:
            messages.info(request, "Credentials not found")
            return redirect(index)
        
    else:
        return render(request,"index.html")



def form(request):
    
    if request.method == "POST":
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        Email = request.POST["email"]
        Phonenumber = request.POST["pnumber"]
        duedate = request.POST["duedate"]
        
        if client.objects.filter(first_name=firstname).exists() and client.objects.filter(last_name=lastname).exists():
            messages.info(request,"Client Already in Database")
        elif client.objects.filter(email=Email).exists():
            messages.info(request,"Client's Email Already in Database")
        else:  
            new = client.objects.create(first_name=firstname, last_name=lastname, email=Email, phone_number=Phonenumber, Duedate= duedate)
            new.save()
            
    else:
        pass
            
            
    clients = client.objects.all()
    
    return render(request,"form.html", {'clients':clients})

def logout(request):
    auth.logout(request)
    return redirect("index")

