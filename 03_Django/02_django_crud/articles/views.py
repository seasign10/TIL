from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect # redirect 
from .models import Article # 현재 폴더(dir)의 models에 있는 Article 가져오기

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk') # DB 가 변경, ORM이기 때문에 이 방법을 권유
    # articles = Article.objects.all[::-1] # python 이 변경
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    try:
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.full_clean() # 전체적으로 검증 (유효성 검증)
    except ValidationError:
        raise ValidationError('Error')
    else: # full_clean에서 검증하고 아무런 문제가 없을때 넘어온다.
        article.save()
    return redirect(f'/articles/{ article.pk }/') # 메인 페이지



def detial(request, pk):
    article = Article.objects.get(pk=pk) # 단일 값을 가져오려면 filter는 부적합, Article이가진 pk : detail함수에서 인자로 받는 pk
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)
    


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/articles/') # DB를 건드렸기 때문에 render는 적합하지 않음


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article}
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)

    article.title = request.POST.get('title') # 기존의 값을 바꾸는것
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}')