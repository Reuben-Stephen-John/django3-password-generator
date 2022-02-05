from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html',{'password':'testing'})
def password(request):
    Characters=list('abcdefghijklmnopqrstuvwxyz')
    length= int(request.GET.get('length',10))
    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        Characters.extend(list('!@#$%&^()'))
    if request.GET.get('numbers'):
        Characters.extend(list('0123456789'))
    thepassword=''
    for i in range(length):
        thepassword+=random.choice(Characters)

    return render(request,'generator/password.html',{'password':thepassword})
def about(request):
    return render(request,'generator/about.html')
