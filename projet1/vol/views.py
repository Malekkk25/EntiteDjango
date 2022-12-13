import ctypes
from imaplib import _Authenticator
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.template import loader
from vol.models import Aeroport, Liste
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import FormConnexion, FormUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

def index(request):
    v = Liste.objects.all().values()
    air=Aeroport.objects.all().values()
    template = loader.get_template('accueil.html')
    context = {
        'v': v,
        'air':air,
    }
    return HttpResponse(template.render(context, request))

def del_vol(request, id):
    vol1 = Liste.objects.get(id=id)
    vol1.delete()
    return HttpResponseRedirect(reverse('vols'))

def list_air(request):
    air=Aeroport.objects.all().values
    template=loader.get_template('aeroport.html')
    context={
        'air':air,
    }
    return HttpResponse(template.render(context,request))
def del_air(request,id):
    aeroport=Aeroport.objects.get(id=id)
    aeroport.delete()
    return HttpResponseRedirect(reverse('aeroports')) 
def update_vol(request,id):
    v=Liste.objects.get(id=id)
    air=Aeroport.objects.all().values()
    template=loader.get_template('updateVol.html')
    context={
        'v':v,
        'air':air,
    }    
    return HttpResponse(template.render(context,request))
def update_vol_action(request,id):
    com=request.POST['compagnie'] 
    pri=request.POST['prixTicket'] 
    dest=request.POST['destination']
    a=request.POST['air']
    aire=Aeroport.objects.get(id=a)
    vol=Liste.objects.get(id=id)
    vol.compagnie=com
    vol.prixTicket=pri
    vol.destination=dest
    vol.air=aire
    vol.save()
    return HttpResponseRedirect(reverse('vols'))

def add_vol(request):
    air=Aeroport.objects.all().values()    
    template=loader.get_template('addVol.html')
    context={
        'air':air,
        
    }
    return HttpResponse(template.render(context,request))

def add_vol_action(request):
    com=request.POST['compagnie'] 
    pri=request.POST['prixTicket'] 
    dest=request.POST['destination']
    a=request.POST['air']
    num=request.POST['numVol']
    date=request.POST['dateDepart']
    aire=Aeroport.objects.get(id=a) 
    v=Liste(numVol=num,prixTicket=pri,destination=dest,compagnie=com,dateDepart=date,air=aire)
    v.save()
    return HttpResponseRedirect(reverse('vols'))

def list_users(request):
    users=User.objects.all().values()
    template=loader.get_template('users.html')
    context={
        'users':users,
    }
    return HttpResponse(template.render(context,request))
    
def del_user(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return HttpResponseRedirect(reverse('users'))  

def create_compte(request):
    user_form=FormUser()
    return render(request, 'createUser.html', {'user_form' : user_form})

def create_user_action(request):
    adrEmail = request.POST['email']
    username = request.POST['login']
    password = request.POST['mot2pass']
    confirm = request.POST['confirm']
    prenom = request.POST['prenom']
    nom = request.POST['nom']   
    if(password==confirm):
        user=User.objects.create_user(username,adrEmail,password)
        user.first_name=prenom
        user.last_name=nom
        user.save()
        return HttpResponseRedirect(reverse('users'))
    else:
        print("Mot de passe et confirmation mot de passe ne sont pas identiques")
        return HttpResponseRedirect(reverse('create_compte'))   

def connect (request):
    connect_form = FormConnexion ()
    return render(request, 'connexion.html', {'connect_form' : connect_form }) 

def signIn(request):
    username = request.POST['login']
    password = request.POST['mot2pass']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username 
        return HttpResponseRedirect(reverse('vols'))
    
    else:
        ctypes.windll.user32.MessageBoxW(0, "Login et/ou mot de passe incorrect", "Erreur", 1)
        return HttpResponseRedirect(reverse('connect'))
def signOut(request):
    logout(request) 
    return HttpResponseRedirect(reverse('connect'))

def update_user(request,id):
    u=User.objects.get(id=id)
    template=loader.get_template('updateUser.html')
    context={
        'u':u
    }    
    return HttpResponse(template.render(context,request))
def update_user_action(request,id):
    prenom = request.POST['prenom']
    nom = request.POST['nom']
    mail = request.POST['mail']
    username = request.POST['login']
    password1 = request.POST['mot2pass']
    ancien=request.POST['ancien']
    admin= request.POST['admin']
    user=User.objects.get(id=id)
    if(not password1):
        user.first_name=prenom
        user.last_name=nom
        user.email=mail
        user.is_staff=admin
        user.username=username   
        user.save()
        return HttpResponseRedirect(reverse('users'))
    if(password1 is not None):
        a = authenticate(request,password=ancien,username=username)
        if(a is not None ):
            user.first_name=prenom
            user.last_name=nom
            user.email=mail
            user.is_staff=admin
            user.set_password(password1)
            user.username=username
            user.save()
            return HttpResponseRedirect(reverse('users'))
        else:
            ctypes.windll.user32.MessageBoxW(0, "Mot de passe et confirmation mot de passe ne sont pas identiques", "Erreur", 1)
            return render(request,'updateUser.html')
            