# 딕셔너리 만들기 -1
# 딕셔너리는 {}
lunch = {
  '중국집': '02-0000-0000'
}

# 딕셔너리 만들기 -2
# 1번 보기 보다 더 빨리 만들 수 있다.
dinner = dict(증국집='02', 일식집='031')


# 딕셔너리에 내용 추가하기
lunch['분식집'] = '031-123-1234'
print(lunch)

# 딕셔너리 내용 가져오기
idol = {
    'bts':{
        '지민': 25,
        'RM': 24,
    }
}

# RM 의 나이는?
idol['bts']['RM']
idol.get('bts').get('RM')

# idol['exo']
# or
#print(idol.get('exo'))


