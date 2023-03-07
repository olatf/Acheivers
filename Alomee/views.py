from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import client
from datetime import date
import requests
import json 

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
        
        if client.objects.filter(first_name=firstname).exists() and client.objects.filter(last_name=lastname).exists() :
            messages.info(request,"Client Already in Database")
        elif client.objects.filter(email=Email).exists():
            messages.info(request,"Client's Email Already in Database")
        else:  
            Clients = client.objects.create(first_name=firstname, last_name=lastname, email=
                               Email, phone_number=Phonenumber, Duedate=duedate)
            Clients.save()
    else:
        pass
        
    clients = client.objects.all()
    
    
    return render(request,"form.html", {'clients':clients})

def sendsms (request):
    
    person = client.objects.all()
    
    today = date.today()
    
    for new in person:
        
        
        Name = new.first_name
        Namelast = new.last_name
        Now = new.Duedate
        Phoneno = new.phone_number
        message ="Hello"+ Name + Namelast + "This is to inform you that your house rent is due and you are required to renew your rents, pls do so as soon as possbile" 
               
        if Now == today: 
            resp = requests.post("https://textbelt.com/text",{
                'phone': Phoneno,
                'message': message,
                'key': 'textbelt',
            })
        else:
            pass    
    
    return render (request, "sendsms.html")

