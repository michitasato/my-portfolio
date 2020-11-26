from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils import timezone

from .models import Post
from .forms import HelloForm



def index(request):
    params = {
        'title': '残業代チェッカー',
        'message': 'your data',
        'form': HelloForm(),
    }
    if (request.method == 'POST'):
        params['message'] = '名前：' + request.POST['name'] + \
        '<br>メール：' + request.POST['mail'] + \
        '<br>年齢：' + request.POST['age']
        params['form'] = HelloForm(request.POST)
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

