from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all() # Meta Data로 ordering을 역순으로 했기 때문에 그대로 가져와도 최신순이 위로 쌓이게 된다.
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)

def create(request):
    # embed()
    if request.method == 'POST':
        # form 인스턴스를 생성하고 요청에 의한 데이터를 인자로 받는다. (binding)
        # 이 처리 과정은 binding 이라고 불리며 유효성 체크를 할 수 있도록 해준다.
        form = ArticleForm(request.POST)
        # embed()
        # form이 유효한지 체크한다.
        if form.is_valid(): # 유효성 검사
            # form.cleaned_data 로 정제된 데이터를 받는다.
            # title = form.cleaned_data.get('title') # 유효성을 통과한 정제된 data
            # content = form.cleaned_data .get('content')
            # article = Article.objects.create(title=title, content=content)
            article = form.save()
            return redirect(article)

        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # # return redirect('articles:index')
        # # models에서 absolute를 만드는 순간
        # return redirect(article) # 인스턴스 객체를 넣으면 detail.html로 간다.
    else:
        form = ArticleForm()
    # 상황에 따라 context 에 넘어가는 2가지 form
    # 1. GER : 기본 form 
    # 2. POST : 검증에 실패 후의 form (is_valid에서 튕겨져 나왔을 때 ==> isvaild == False)
    context = {'form': form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comment_set.all() # _set은 고정값 앞은 모델명 / article의 모든 댓글
    comment_form = CommentForm() # 댓글 폼
    context = {'article': article, 'comment_form': comment_form, 'comments': comments,}
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # else:
    #     return redirect(article)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        # embed()
        if form.is_valid():
            # article.title = form.cleaned_data.get('title')
            # article.content = form.cleaned_data.get('content')
            # article.save()
            article = form.save()
            return redirect(article)
    else:
        # ArticleForm 을 초기화 (이전에 DB에 저장된 데이터를 넣어준 상태)
        # form = ArticleForm(initial={'title': article.title, 'content': article.content})
        # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
        # form = ArticleForm(initial=article.__dict__)
        form = ArticleForm(instance=article)

    # 1. POST : 검증에 실패한 form(오류 메세지도 포함된 상태)
    # 2. GET : 초기화된 form
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)

@require_POST
def comments_create(request, article_pk):
    # if request.method == 'POST':
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid(): # True가 나온다면
        # 객체를 Create 하지만 DB에 레코드는 작성하지 않는다.
        comment = comment_form.save(commit=False) # comment는 만들어졌지만 save는 되지 않은상태
        comment.article_id = article_pk # 객체(article)를 통째로 사용하기에는 article이 만들어지지 않은 상태기 때문에 article_pk를 이용한다.
        comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    # if request == 'POST':
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete
    return redirect('articles:detail', article_pk)