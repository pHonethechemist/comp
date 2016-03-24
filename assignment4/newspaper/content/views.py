from django.shortcuts import render

from models import Article, Image, Contributor

def all_articles(request):
  data = {'articles': Article.objects.all()}
  return render(request, 'all_articles.html', data)
