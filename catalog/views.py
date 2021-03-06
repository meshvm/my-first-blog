from django.shortcuts import render
from django.utils import timezone
from .models import Post

def library_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'catalog/library_list.html', {'posts': posts})
# Create your views here.
