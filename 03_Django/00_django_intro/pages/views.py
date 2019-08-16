# django imports style guide
# 1. standard library (ex. random)
# 2. third-party (ex. requests)
# 4. Django
# 5. local django

import requests
import random
from datetime import datetime
from django.shortcuts import render
from pprint import pprint

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'pages/index.html') # render()의 첫번째 인자도 반드시 request



def introduce(request, name, age):
    context = {'name': name, 'age': age,}
    return render(request, 'pages/introduce.html', context)



def dinner(request):
    menu = ['족발', '햄버거', '치킨', '라멘']
    pick = random.choice(menu)
    return render(request, 'pages/dinner.html', {'pick': pick,}) # 앞의pick은 tamplates에서 가져오는 pick (다른 것), 통상적으로 이름을 똑같이 맞춤.



def image(request):
    return render(request, 'pages/image.html')



def hello(request, name): # name은 변수, 이름이 달라도 상관이 없다.
    menu = ['족발', '햄버거', '치킨', '라멘']
    pick = random.choice(menu)
    context = {'name': name, 'pick': pick,} # 오른쪽의 name이 함수 name
    return render(request, 'pages/hello.html', context)



def times(request, num1, num2):
    mul = num1 * num2
    context = {'mul': mul, 'num1': num1, 'num2': num2,}
    return render(request, 'pages/times.html', context)



def area(request, r):
    area = (r ** 2) * 3.14
    context = {'r': r, 'area': area,}
    return render(request, 'pages/area.html', context)



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
    return render(request, 'pages/template_language.html', context)

def isitgwangbok(request):
    today = datetime.now()
    if today.month == 8 and today.day == 15:
        result = True
    else:
        result = False
    context = {'result': result,}
    return render(request, 'pages/isitgwangbok.html', context)



def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    # pprint(request)
    # pprint(request.scheme)
    # pprint(request.method)
    # pprint(request.GET)
    # pprint(request.meta)
    message = request.GET.get('message') # message 신호를 받을 코드(message라는 dictionary를 받음), 여기서의 get은 값을 받아오는 것. GET != get
    context = {'message': message,}
    return render(request, 'pages/catch.html', context)



def art(request):
    return render(request, 'pages/art.html')

def result(request):
    # 1. art에서 form으로 보낸 데이터를 받는다.
    word = request.GET.get('word')

    # 2. ARTII API 폰트 리스트로 요청을 보내 응답을 text로 받는다.
    fonts = requests.get('http://artii.herokuapp.com/fonts_list').text
    
    # 3. str 을 list로 바꾼다.
    fonts = fonts.split('\n')

    # 4. fonts list 안에 들어있는 요소 중 하나를 선택해서 변수에 저장
    font = random.choice(fonts)

    # 5. 위에서 만든 word와 font를 가지고 다시 요청을 만들어서 보내 응답결과를 받는다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    context = {'response': response,}
    return render(request, 'pages/result.html', context)



def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    name = request.POST.get('name')
    pwd = request.POST.get('pwd')
    context = {'name': name, 'pwd': pwd,} # 값을 원래는 저장해야하지만 출력값만 보기위해서 쓰여진 코드
    return render(request, 'pages/user_create.html', context)



def static_example(request):
    return render(request, 'pages/static_example.html')