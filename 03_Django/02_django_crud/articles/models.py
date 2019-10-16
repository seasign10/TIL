from imagekit.models import ProcessedImageField, ImageSpecField # ImageSpecField 원본을 불러서 원본으로 부터 자르는 작업을 해서 원본도 저장이 된다.
from imagekit.processors import Thumbnail # Thumbnail은 잘라주는 기능


from django.urls import reverse
from django.db import models

def articles_image_path(instance, filename):
    return f'articles/{instance.pk}/images/{filename}'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # 이미 만들어진 테이블에 추가되었기 때문에 테이블 순서상 가장 마지막에 붙는다.
    # 가운데 넣은 이유는 아래의 create_at과 update_at이 models.py에서 보기에 마지막에 붙는게 보기 좋기 때문
    
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     # 위의 image로 부터 만들어 지기 때문에 서로 연결을 시켜주어야 한다.
    #     source='image',
    #     processors=[Thumbnail(200, 300)],
    #     format='JPEG',
    #     options={'quality': 90},
    # )

    image = ProcessedImageField(
        # ProcessedImageField 에 인자로 들어가 있는 값들은 migrations 이후에 추가되거나
        # 수정이 되더라도 makemigrations 를 하지 않아도 된다.
        processors=[Thumbnail(200, 300)], # 처리할 작업 목록
        format='JPEG', # 저장 포맷
        options={'quality': 90}, # 추가 옵션들
        upload_to='articles/images', # 저장 위치(MEDIA_ROOT/article/images) / media폴더는 생략되어 있다
    )
    
    # image = models.ImageField(blank=True) # 빈값이 허용이 되는 컬럼이 되어 사진오류가 나지 않음
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        # return f'/articles/{self.pk}/'
        # return reverse('articles:detail', args=[self.pk]) # articles/pk값/ => 문자열로 나타난다.
        # return reverse('articles:detail', kwargs={'key': self.pk})
        return reverse('articles:detail', kwargs={'article_pk': self.pk})

        # 주의 사항
        # reverse 함수에 args 와 kwargs를 동시에 인자로 보낼 수 없다.
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk'] # 가장 최신 댓글이 위로 올라오도록

    def __str__(self):
        # return self.content
        return f'<Article({self.article_id}): Comment({self.pk})-{self.content}'