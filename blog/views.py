from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,Comment
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name')!=None:
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username')!=None:
        posts= posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name')!=None:
        posts = posts.filter(tags__name__in = [kwargs['tag_name']])

    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single_view(request,pid):
    Comment.name = 'Unknown'
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'thanks your comment sent successfuly.')
        else:
            messages.add_message(request,messages.ERROR,'your comment didnt sent successfuly.')

    form = CommentForm
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    if not post.login_require:
        comments = Comment.objects.filter(post=post.id,approve=True).order_by('-created_date')
        context = {'post':post,'comments':comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def test(request):
    return render(request,'test.html')


def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name = cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_search(request):
    posts = Post.objects.filter(status=1)

    if request.method == 'GET':
        if request.GET.get('s'):
            posts = posts.filter(content__contains = request.GET.get('s'))
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def home_post(request):
    posts = Post.objects.filter(status=1).order_by('published_date')
    context = {'posts':posts}
    return render(request,'website/index.html',context)