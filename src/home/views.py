from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
# def home_view(request):
#   template_name = "base.html"
#   return render(request, template_name)

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'