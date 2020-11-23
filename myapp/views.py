from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    params = {
        'title': 'Hello/index',
        'msg':'これはサンプルページです',
        'goto': 'next',
    }
    return render(request, 'myapp/index.html', params)

def next(request):
    params = {
        'title': 'Hello/Next',
        'msg':'これはもう１ページです',
        'goto': 'index',
    }
    return render(request, 'myapp/index.html', params)
