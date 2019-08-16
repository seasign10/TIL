from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index) # 자기자신에 있는 index
]