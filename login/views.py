from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == "POST":
        title = request.POST['title']
        location = request.POST['location']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        print('User Created')
        return redirect('/start')
    else:
        return render(request, 'inv/register.html')
