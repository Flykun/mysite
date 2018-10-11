from django.shortcuts import render
from django.core.paginator import Paginator

from blog.models import BlogType, Blog


def home(request):
    context = {}
    return render(request, 'blog/home.html', context)


def blog_list(request):
    contact_list = Blog.objects.all()
    paginator = Paginator(contact_list, 2)

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    return render(request, 'blog/blog_list.html',
                  {'paginator': paginator, 'contacts': contacts})


def blog_detail(request, blog_pk):
    blog = Blog.objects.get(pk=blog_pk)

    previous_blog = Blog.objects.filter(
        created_time__gt=blog.created_time).last()
    next_blog = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context = {'blog': blog,
               'previous_blog': previous_blog,
               'next_blog': next_blog
               }
    return render(request, 'blog/blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):
    blog_type = BlogType.objects.get(pk=blog_type_pk)
    type_blogs = Blog.objects.filter(blog_type__pk=blog_type_pk)
    blog_all_list = Blog.objects.filter(blog_type=blog_type)
    context = {'blogs': type_blogs, 'blog_type': blog_type}
    return render(request, 'blog/blogs_with_type.html', context)
