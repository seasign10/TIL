from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect # redirect 
from .models import Article, Comment # 현재 폴더(dir)의 models에 있는 Article, Comment 가져오기

# Create your views here.
def index(request):
    # embed()
    articles = Article.objects.order_by('-pk') # DB 가 변경, ORM이기 때문에 이 방법을 권유
    # articles = Article.objects.all[::-1] # python 이 변경
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


# def new(request):
#     return render(request, 'articles/new.html')


def create(request):
    # CREATE
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect(article) # 메인 페이지
    #NEW
    else:
        return  render(request,'articles/create.html')




def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk) # 단일 값을 가져오려면 filter는 부적합, Article이가진 pk : detail함수에서 인자로 받는 pk
    comments = article.comment_set.all() # 특정 article 에 있는 comment를 가져와야 한다.
    context = {'article': article, 'comments': comments,}
    return render(request, 'articles/detail.html', context)
    


def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('/articles/') 
    else:
        return redirect(article)


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}
#     return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title') # 기존의 값을 바꾸는것
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {'article': article,}
        return render(request, 'articles/update.html', context)
        
def comment_create(request, article_pk):
    # 댓글을 달 게시글
    article = Article.objects.get(pk=article_pk) # 추후에 댓글을 삭제하기위한 대비, 댓글과 댓글이 달린 게시글의 값 둘 다 필요하다
    if request.method == 'POST':
        # pass # pass를 먼저 코드를 작성 후에 GET방식을 받고, 나중에 수정해주는 것이 좋다.
        
        # form 에서 넘어온 댓글 정보
        content = request.POST.get('content')
        #댓글 생성 및 저장
        comment = Comment(article=article, content=content) # content는 부모의 객체를 가지고 있기때문에 부모의 객체를 먼저 넣어주어야한다.
        #article=article에서 알아서 pk값이 들어간다.
        comment.save()
        return redirect(article)
        # return redirect('article:detail' artucke.pk)
        # return redirect('article:detail' artucke_pk)

    else:
        return redirect(article)

def comment_delete(request, article_pk, comment_pk):
    # comments = article.comment_set.all()
    # article = Article.objects.get(pk=article_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST':
        comment.delete()
    # return redirect(article) # 어차피 같은곳으로 return하기 때문에 if문 밖에서 쓰면 불필요한 반복문을 줄일 수 있다.
    return redirect('articles:detail', article_pk)

