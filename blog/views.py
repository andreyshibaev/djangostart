from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Blog


def myblog(request):
    allposts = Blog.objects.all()
    # allposts = get_list_or_404(Blog)
    context = {
        'allposts': allposts,
    }
    return render(request, 'blog/listarticles.html', context)


def showpost(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blog/showpost.html', {'post': post})