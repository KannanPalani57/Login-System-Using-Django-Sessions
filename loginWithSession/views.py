from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        if username == "root" and password == "password":
            request.session['logged_in'] = True
            return render(request, "secret.html")
    return render(request, "login.html")

def secretPage(request):
    if not request.session.get('logged_in'):
        return render(request, "login.html")
    return render(request, "secret.html")


def logout(request):
    try:
        del request.session['logged_in']
    except KeyError:
        return redirect("login")   
    return render(request, "logout.html")     