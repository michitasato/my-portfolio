from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    params = {
        'title': 'Hello/index',
        'msg':'これはサンプルページです',
    }
    return render(request, 'myapp/index.html', params)
