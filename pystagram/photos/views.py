from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    return HttpResponse('hewllo world')


def list_posts(request):
    ctx = {}
    return render(request, 'list.html', ctx)
