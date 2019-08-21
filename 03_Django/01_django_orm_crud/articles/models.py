from django.db import models

# Create your models here.
class Article(models.Model): # models.Model의 상속을 받는다.
    # 클래스 변수 (DM의 필드), 4개의 colum을 만듦, 소문자로 만들어야 한다.

    # id(프라이머리 키)는 기본적으로 처음 테이블 생성이 자동으로 만들어진다'
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10) # 글자수를 제한하는 문자열로 들어갈 것, 최대 10글자
    content = models.TextField() # 위와 달리 제한이 없는 대규모 필드
    created_at = models.DateTimeField(auto_now_add=True) # 날짜와 시간을 계산해주는 필드
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'
    