from django.urls import path
from . import views

urlpatterns = [
    # 원래 app url 은 아래로 작성해 나간다.
    # setting app 등록과 같은 것들은 위로 계속 쌓아가지만 얘만 유일하게 아래로 작성한다.
    # alt 키를 누른채로 방향키를 위 아래로 움직이면 한 줄씩 방향키대로 자리가 바뀐다.
    path('index/', views.index),
    path('introduce/<name>/<int:age>/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<str:name>/', views.hello), # str은 기본값이기 때문에 생략 가능 => <name>
    path('times/<int:num1>/<int:num2>/', views.times),
    path('area/<int:r>/', views.area),
    path('template_language/', views.template_language),
    path('isitgwangbok/', views.isitgwangbok),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]