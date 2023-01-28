from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
from django.shortcuts import render
from django.core.paginator import Paginator


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single_view(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    context = {'post':post}
    return render(request,'blog/blog-single.html',context)

def test(request,pid):
    posts = Post.objects.filter(id=pid)
    context = {'posts':posts}
    return render(request,'test.html',context)

    

# def listing(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 1) # Show 1 contacts per page.
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/blog-single.html', {'posts': page_obj})

