from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY'
    
@app.route('/dday')
def dday():
    # 오늘 날짜
    today_time = datetime.now()
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time
    return f'{dday.days} 일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML TAG</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러 줄을 보내 봅시다</h1>
    <ul>
        <li>1111</li>
        <li>2222</li>
    </ul>
    """

@app.route('/greeting/<name>')
# @app.route('/greeting/<string:name>') 위 아래 같음
def greeting(name):
    return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:number>')
def cube(number):
    #연산을 모두 끝내고 변수만 cube.html로 넘긴다.
    result = number**3
    return render_template('cube.html', result=result, number=number)
    
@app.route('/movie')
def movie():
    movies = ['어벤져스', '저스티스', '메이즈러너', '라라랜드', '위대한 쇼맨']
    return render_template('movie.html', movies=movies )

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # print(request.args)
    name = request.args.get('data') #ping에서 입력한 문자가 들어있음
    return render_template('pong.html', name=name)

# # /lunch/몇명이 식사하는지 인원
# # 플라스크는 여러 메뉴 중에서 인원 수만큼의 메뉴를 응답합니다.
import random
@app.route('/lunch/<int:number>')
def lunch(number):
    menu = ['계란말이', '고등어 조림', '카레', '칼국수', '게장']
    lunch = random.sample(menu, number)
    return f'오늘의 점심은 {lunch}'
    #return str(lunch)를 해도 됨


@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/recieve')
def recieve():
    return render_template('recieve.html')


import random
@app.route('/print_answer')
def answer():
    name = request.args.get('data')
    past = ['부자집 고양이', '가난뱅이 머릿속의 이', '이루어질 수 없는 사랑의 줄리엣', '레고를 밟고 사망한 귀족']
    life = random.choice(past)
    return render_template('print_answer.html', life=life, name=name)

