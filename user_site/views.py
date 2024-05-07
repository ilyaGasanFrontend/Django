from django.shortcuts import render
from .models import Article

def index(request):
    if request.method == 'POST':
        userName = request.POST['userName']
        InputEmail = request.POST['InputEmail']
        phonenumber = request.POST['phonenumber']
        university = request.POST['university']
        sciAdviser = request.POST['sciAdviser']
        article = request.POST['article']
        FormControlTextarea1 = request.POST['FormControlTextarea1']
        new_article = Article(username=userName, email=InputEmail,
            phonenumber=phonenumber,
            university=university,
            adviser=sciAdviser, article=article,
            about=FormControlTextarea1)
        new_article.save()
    articles = Article.objects.all()
    active_article = articles.first()
    return render(request, 'index.html', {'articles': articles, 'active_article': active_article})

def show_articles(request):
    articles = Article.objects.all()
    return render(request, 'show_articles.html', {'articles': articles})
    