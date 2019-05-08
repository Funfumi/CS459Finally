from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate,logout,login as auth_login

from django.http import HttpResponse
import datetime
from .models import Item

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# def home(request):
#     context={'key':'value', 'name':'Hello Wasit!'}
#     return render(request, 'home.html', context)

def item_list(request):
    context = {'items' : Item.objects.all()}
    return render(request, 'item_list.html', context)   

def store(request):
    context = {'items' : Item.objects.all()}
    return render(request, 'store.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')

def login(request):
    context = {'items' : Item.objects.all()}
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print("auth",str(authenticate(username=username, password=password)))

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                auth_login(request, user)
                return redirect('store')
        else:
            return redirect('login_page')
    else:
        # Bad login details were provided. So we can't log the user in.
        # print ("Invalid login details: {0}, {1}".format(username, password))
    #     return HttpResponse("Invalid login details supplied.")
    # else:

        return render(request, 'login.html', context)

# def register(request):
#     context = {'items' : Item.objects.all()}
#     return render(request, 'register.html', context)

def cart(request):
    context = {'items' : Item.objects.all()}
    return render(request, 'cart.html', context)

def storeAdmin(request):
    context = {'items' : Item.objects.all()}
    return render(request, 'storeAdmin.html', context)

def register(request):
    context = {'items' : Item.objects.all()}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', context)
    # return render(request, 'register.html'),{'form' : form}

# def login(request):
#     context = RequestContext(request)
#     if request.method == 'POST':
#         # Gather the username and password provided by the user.
#         # This information is obtained from the login form.
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username)
#         print(password)
#         user = authenticate(username=username, password=password)
#         print("auth",str(authenticate(username=username, password=password)))

#         if user:
#             # Is the account active? It could have been disabled.
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#         else:
#             return HttpResponse("/")
#     else:
#         # Bad login details were provided. So we can't log the user in.
#         print ("Invalid login details: {0}, {1}".format(username, password))
#         return HttpResponse("Invalid login details supplied.")
#     else:
#         return render_to_response('user/profile.html', {}, context)







