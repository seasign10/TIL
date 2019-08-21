from django.contrib import admin
from .models import Article  # 명시적 상대경로 표현

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # 튜플이나 리스트로 작성한다. 대부분 튜플로 작성되어 있다.
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)
    
    # 필더를 만드는것, created_at은 시간별로 필터링을 해준다.
    list_filter = ('created_at',)

    # 링크를 거는것 (클릭하면 해당 content 수정 페이지로 이동)
    list_display_links = ('content',)

    # 바로 수정가능하게 만드는 것
    list_editable = ('title',)

    # 값을 넣지 않으면 기본값 100
    list_per_page = 2

admin.site.register(Article, ArticleAdmin) # ArticleAdmin 만들고 레지스터에 등록
