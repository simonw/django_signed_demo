from django.shortcuts import render_to_response as render
from django.http import HttpResponseRedirect, HttpResponse
from pprint import pformat

def index(request):
    return render('index.html', {
        'user': request.get_signed_cookie('user', default = None),
        'cookies': pformat(request.COOKIES),
        'user_cookie': request.COOKIES.get('user', ''),
    })

def login(request):
    username = request.POST.get('username', '').strip()
    password = request.POST.get('password', '').strip()
    if username and password and username == password:
        response = HttpResponseRedirect('/')
        response.set_signed_cookie('user', username)
        return response
    else:
        return HttpResponse('Username and password did not match')

def tamper(request):
    response = HttpResponseRedirect('/')
    response.set_cookie('user', request.POST.get('cookie', ''))
    return response
