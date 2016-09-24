from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from .models import Post
from .forms import PostSimpleForm
from .forms import PostForm
# Create your views here.

def hello_world(request):
    return HttpResponse('hewllo world')


def list_posts(request):
    page = request.GET.get('page', 1) #dictionary 에서 get(이거가져오고, 없으면 이거(1) )
    per_page = 2

    posts = Post.objects.all().order_by('-created_at')
    pgt = Paginator(posts, per_page)

    try:
        contents = pgt.page(page)
    except PageNotAnInteger:
        contents = pgt.page(1)
    except EmptyPage:
        contents = []

    ctx = {
        'posts': contents,
    }

    return render(request, 'list.html', ctx)


def view_post(request, pk):
#    post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    ctx = {}
    return render(request, 'view.html', ctx)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            #post = Post()
            #post.content = form.cleaned_data['content']
            #post.save()
            post = form.save() # 위 세줄을 한줄로 줄임

            return redirect('photos:view_post', pk=post.pk)

    elif request.method == 'GET':
        form = PostForm()

    ctx = {
        'form': form,
    }

    return render(request, 'edit.html', ctx)
