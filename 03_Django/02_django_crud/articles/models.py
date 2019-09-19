from django.urls import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
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