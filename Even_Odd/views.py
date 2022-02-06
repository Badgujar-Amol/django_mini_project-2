from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    c =''
    value = {}
    if request.method =='POST':
        n = eval(request.POST.get('num1'))
        if n % 2 == 0:
            c = 'Even Number '
        else:
            c = 'Odd Number'

        value = {
            'n' : n,
            'c' : c
        }
    print(c)
    return render (request, 'home.html',value)