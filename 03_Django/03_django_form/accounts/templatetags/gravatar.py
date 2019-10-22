import hashlib
from django import template

register = template.Library() # 기본 템플릿 라이브러리에

# 아래의 함수를 추가한다.
@register.filter # django 가 인식하도록 데코레이터 추가, => 필터로 인식이 됨
def makemd5(email): # filter 앞의 인자 (이름은 크게 상관 없음)
    return hashlib.md5(email.encode('utf-8').lower().strip()).hexdigest()