from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'mygenerator/index.html')


def generate_password(request):
    length = int(request.GET.get('length'))
    res_start = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('upper'):
        res_start.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        res_start.extend(list('0123456789'))
    if request.GET.get('special'):
        res_start.extend(list('!@#$%^&*()'))

    res_end = ''
    for _ in range(length):
        res_end += random.choice(res_start)
    return render(request, 'mygenerator/your-password.html', {'password': res_end})


# mwwww
def about(request):
    return render(request, 'mygenerator/about.html')
