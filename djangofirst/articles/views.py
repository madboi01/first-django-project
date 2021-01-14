from django.shortcuts import render
from .models import Article

# Create your views here.

def articles_list(request):
    articles=Article.objects.all().order_by('data')
    return render(request,'articles/articles.html',{'articles':articles})