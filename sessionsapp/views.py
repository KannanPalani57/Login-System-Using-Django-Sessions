from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Home Page")

def saving_session(request):
    request.session['id'] = 6
    request.session['name'] = "yourName"
    return HttpResponse("The Session data saved...")    

def view_sessionData(request):
    response = ""
    if request.session.get('id'):
        response += "The session id is {0} <br>".format(request.session.get('id'))
    if request.session.get('name'):
        response += "The session id is {0} <br>".format(request.session.get('name'))
    if not response:
        return HttpResponse("No session data")
    return HttpResponse(response)    

def delete_session_data(request):
    try:
        del request.session['id']
        del request.session['name']
    except KeyError:
        pass

    return HttpResponse("Session Data cleared")