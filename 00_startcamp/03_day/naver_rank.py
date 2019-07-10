import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com/'

# 요청 보내서 html 파일 받고

html = requests.get(url).text

# 뷰숲으로 정체

soup = BeautifulSoup(html, 'html.parser')

# select 메서드로 사용해서 list 를 얻어낸다

rank = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a .ah_k')
for i in rank:
    print(i.text)
# 뽑은 list를 with 구문으로 잘 작성해보자.(txt)

with open('naver_rank.txt', 'w') as f:
    for i in rank:
        f.write(f'{i.text}\n')







'#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(15) > a > span.ah_r'
'#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(15) > a > span.ah_k'