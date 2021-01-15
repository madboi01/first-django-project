from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.

def articles_list(request):
    articles=Article.objects.all().order_by('data')
    return render(request,'articles/articles.html',{'articles':articles})

def article_detail(request,slug):
    #return HttpResponse(slug)
    article=Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article})