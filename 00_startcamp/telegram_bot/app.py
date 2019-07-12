from flask import Flask, render_template, request 
import requests
from decouple import config

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')





@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 데이터 구조 print 해보기
    # print(request.get_json())
    from_telegram = request.get_json()

    if from_telegram.get('message') is not None:
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')

        # 한글 키워드 받기

        #/번역 (띄어쓰기 한 칸 중요!)으로 입력이 시작된다면, 파파고로 번역이 동작한다.
        if text[0:4] == '/번역 ':
            headers = {
                # 네이버에서 주는 링크들과 아이디, 등은 개인의 중요 정보가 포함되어 있으므로, env대체 해준다.
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret
            }
            data = {'source': 'ko', 'target': 'en', 'text': text [4:]}
            # requests.post를 쓰는 이유는 개인 정보가 담긴 headers와 data가 있기 때문이다. 왼쪽의 https:// 주소 아래로 코드가 들어가게 되어 드러나지 않게 한다.
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            # print(papago_res.json()) => 출력을 해서 json으로 이 구문에 대한 딕셔너리를 얻어낸다. 따로 정리해서 .get()을 좀더 쉽게 사용할 수 있다.
            text = papago_res.json().get('message').get('result').get('translatedText')

        # 로또 당첨 봇

        if text[0:4] == '/로또 ':
            # 회차 번호를 받아온다.
            num = text[4:]
            # 동행 복권에 요청을 보내 응답을 받는다.
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            # json 형태로 바꿔준다. 
            lotto = res.json()

            # 당첨번호 6개만 가져오기
            winner = []
            for i in range(1, 7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            text = f'로또 {num} 회차의 당첨 번호는 {winner}입니다. 보너스 번호는 {bonus_num}입니다.'




        # requests.get은 한 줄만 써주면 된다. 번역을 늘리고 싶으면 위의 if문을 복사해서 추가하면 된다.
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')


    return '', 200