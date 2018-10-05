from django.shortcuts import render
from blog.models import BlogType, Blog


def blog_list(request):
    context = {'blogs': Blog.objects.all()}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, blog_pk):
    context = {'blog': Blog.objects.get(pk=blog_pk)}
    return render(request, 'blog/blog_detail.html', context)


def blogs_with_type(request, blog_type_pk):
    blog_type = BlogType.objects.get(pk=blog_type_pk)
    type_blogs = Blog.objects.filter(blog_type__pk=blog_type_pk)
    context = {'blogs': type_blogs, 'blog_type':blog_type}
    return render(request, 'blog/blogs_with_type.html', context)
