# django imports style guide
# 1. standard library (ex. random)
# 2. third-party (ex. requests)
# 4. Django
# 5. local django

import random
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html') # render()의 첫번째 인자도 반드시 request



def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'introduce.html', context)



def dinner(request):
    menu = ['족발', '햄버거', '치킨', '라멘']
    pick = random.choice(menu)
    return render(request, 'dinner.html', {'pick': pick,}) # 앞의pick은 tamplates에서 가져오는 pick (다른 것), 통상적으로 이름을 똑같이 맞춤.



def image(request):
    return render(request, 'image.html')



def hello(request, name): # name은 변수, 이름이 달라도 상관이 없다.
    menu = ['족발', '햄버거', '치킨', '라멘']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,} # 오른쪽의 name이 함수 name
    return render(request, 'hello.html', context)



def times(request, num1, num2):
    mul = num1 * num2
    context = {'mul': mul, 'num1': num1, 'num2': num2,}
    return render(request, 'times.html', context)



def area(request, r):
    area = (r ** 2) * 3.14
    context = {'r': r, 'area': area,}
    return render(request, 'area.html', context)



def template_language(request):
    menus = ['잡채밥', '짬뽕', '마라탕', '마랴텐지투이',]
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'bansns', 'cucumber', 'bean',]
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }
    return render(request, 'template_language.html', context)

def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'isitgwangbok.html', context)