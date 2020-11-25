from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils import timezone

from .models import Post


def index(request):
    params = {
        'title': 'Hello/index',
        'msg':'お名前は？',
        'goto': 'next',
    }
    return render(request, 'myapp/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title': 'Hello/Form',
        'msg': 'こんにちは' + msg + 'さん。',
        }
    return render(request, 'myapp/index.html', params)

def next(request):
    params = {
        'title': 'Hello/Next',
        'msg':'これはもう１ページです',
        'goto': 'index',
    }
    return render(request, 'myapp/index.html', params)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/post_list.html', {'posts': posts})

