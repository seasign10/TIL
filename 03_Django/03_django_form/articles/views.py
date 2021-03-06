from IPython import embed
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse
from django.views.decorators.http import require_POST
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):

    # session에 visits_num 키로 접근해 값을 가져온다.
    # 기본적으로 존재하지 않는 키이기 때문에 키가 없다면(즉 방문한적이 없다면 = 첫 방문) 0 값을 가져오도록 한다.
    visits_num = request.session.get('visits_num', 0)
    # 그리고 가져온 값을 session에 visits_num 에 매번 1씩 증가한 값으로 할당한다.
    request.session['visits_num'] = visits_num + 1
    # session data 안에 있는 새로운 정보를 수정했다면 django는 수정한 사실을 알아채지 못하기 때문에 다음과 같이 설정.
    request.session.modified = True





    articles = Article.objects.all() # Meta Data로 ordering을 역순으로 했기 때문에 그대로 가져와도 최신순이 위로 쌓이게 된다.
    context = {'articles': articles, 'visits_num': visits_num,}
    return render(request, 'articles/index.html', context)

@login_required
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
            article = form.save(commit=False)
            # article.user_id = request.user.pk
            # 객체를 가져올 수 있다면 객체 자체를 그대로 넣어준다.
            article.user = request.user
            article.save()
            # Hashtag : 글이 다 작성된 이후에 해시태그가 생성 됨
            for word in article.content.split(): # content를 공백 기준으로 리스트로 변경
                if word.startswith('#'): # '#'으로 시작되는 요소만 선택
                    # word랑 같은 해시태그를 찾는데 있으면 기존 객체, 없으면 새로운 객체를 생성
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag)
            
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
    person = get_object_or_404(get_user_model(), pk=article.user_id) # user.pk도 가능하지만 가능한 최소화 하는게 좋다.
    comment_form = CommentForm() # 댓글 폼
    context = {'article': article, 'comment_form': comment_form, 'comments': comments, 'person': person,}
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated: # 인증이 된 회원인지 아닌지 검열 후,
        article = get_object_or_404(Article, pk=article_pk)
        if request.user == article.user:
        # if request.method == 'POST':
            article.delete()
        else:
            return redirect(article)
    return redirect('articles:index')
    # else:
    #     return redirect(article)

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article) # binding 작업 (instance : modelform에서 initial의 역할)
            if form.is_valid(): # 유효성 검증
                # article.title = form.cleaned_data.get('title') # 가져온 데이터(article.title)에 바꿔서 넣어준다.
                # article.content = form.cleaned_data.get('content') # 가져온 데이터(article.content)에 바꿔서 넣어준다.
                article = form.save()

                # hashtag
                article.hashtags.clear() # 해당 article의 hashtag 전체 삭제(이 구문만 추가됨)
                # for문은 create 작성할 때와 동일
                for word in article.content.split():
                    if word.startswith('#'):
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)
                return redirect(article)
        else:
            # embed()
            # ArticleForm 을 초기화 (이전에 DB에 저장된 데이터를 넣어준 상태)
            # form = ArticleForm(initial={'title': article.title, 'content': article.content}) # initial : 기존의 값을 가져온다(딕셔너리 형태로!)
            # __dict__ : article 객체 데이터를 딕셔너리 자료형으로 변환
            # form = ArticleForm(initial=article.__dict__)
            form = ArticleForm(instance=article)
            # 위와 같이 복잡한 한 줄은 매직 머서드(__dict__)로 줄여서 쓸 수 있다.
    else:
        return redirect('articles:index')
    # 1. POST 방식일 때 넘어오는 form => 검증에 실패한 form(오류 메세지도 포함된 상태의 form)
    # 2. GET 방식일 때 넘어오는 form => 초기화된 form
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context) # 서로 form을 쓰므로 create.html을 빌려와서 쓴다.(template은 공유하는 상태)


@require_POST
def comments_create(request, article_pk):
    if request.user.is_authenticated:
    # if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid(): # True가 나온다면
            # 객체를 Create 하지만 DB에 레코드는 작성하지 않는다.
            comment = comment_form.save(commit=False) # comment는 만들어졌지만 save는 되지 않은상태
            comment.article_id = article_pk # 객체(article)를 통째로 사용하기에는 article이 만들어지지 않은 상태기 때문에 article_pk를 이용한다.
            comment.user_id = request.user.pk
            comment.save()
    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
    # if request == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
            return redirect('articles:detail', article_pk)
        else:
            return redirect('articles:detail', article_pk)
    return HttpResponse('You are Unauthorized', status=401)

@login_required
def like(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # get 유일한 값만 출력, filter 값이 없어도 빈값 출력
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_users.add(request.user)

    # 해당 게시글에 좋아요를 누른 사람들 중에서 현재 접속 유저가 있다면 좋아요를 취소
    # if request.user in article.like_users.all():
    #     article.like_users.remove(request.user) # 좋아요 취소
    # else:
    #     article.like_users.add(request.user) # 좋아요 활성
    return redirect('articles:index')

@login_required
def follow(request, article_pk, user_pk):
    # 게시글 유저
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 접속 유저
    user = request.user

    if person != user:
        # 내(user)가 게시글 유저(person) 팔로워 목록에 이미 존재 한다면,
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(user)
    return redirect('articles:detail', article_pk)

    # if user in person.follower.all():

def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles = hashtag.article_set.order_by('-pk')
    context = {'hashtag':hashtag, 'articles':articles,}
    return render(request, 'articles/hashtag.html', context)