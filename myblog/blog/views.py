# Create your views here.
from .models import Blog, Comments
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_blog_list'

    def get_queryset(self):
        blogs = Blog.objects.filter(create_time__lte=timezone.now()).order_by('-create_time')
        return blogs


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'the_blog'


# def detail(request, pk):
#     the_blog = Blog.objects.get(id=pk)
#     context = {'the_blog': the_blog}
#     return render(request, 'blog/detail.html', context)
def add_comment(request, pk):
    the_blog = Blog.objects.get(id=pk)
    context = {'the_blog': the_blog}
    return render(request, 'blog/add_comment.html', context)
