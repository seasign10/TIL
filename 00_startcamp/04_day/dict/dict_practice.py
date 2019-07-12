"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
scores = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
total_score = 0
for subject_score in scores.values():
    total_score = total_score + subject_score
    # total_score += subject_score 위의 식과 동일, 너무 길어서 나온 식

avg_score = total_score / 3
#avg_score = total_score / len(socres) => length은 길이. 해당 키의 갯수만큼 나눠짐.
print(avg_score)



# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

total_score = 0
count = 0
# for 문을 카운트 하기 위해 만듦

for person_score in scores.values():
    for indivisual_score in person_score.values():
        total_score = total_score + indivisual_score
        count = count + 1

avg_score = total_score / count
print(avg_score)




# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# value가 list임
for name, temp in city.items():
    # name = 서울
    # temp = [-6, -10, 5] len(temp) => 3
    avg_temp = sum(temp) / len(temp)
    print(f'{name} : {avg_temp:.1f}')
    # .1f => 소수점 하나만 출력하겠다. - 찾아서 씀 외우기 x




# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')

# for을 첫번째로 돌 때, 기준 지역, 기준 온도 : 서울
# 두번째 for문이 들어왔을 때, 서울과 비교하게 될 것.
# 첫 for문 때 서울이 가장 온도가 높은 곳은 서울 이었다가 2번째 3번째 for문이 계속 돌면서 가장 높은 온도인 지역으로 값을 갈아치움

count = 0
for name, temp in city.items():
    # 첫 번째 시행 때
    # name = '서울'
    # temp = [-6, -10, 5]
    # 계속 갈아치우는게 아닌 비교한 다음에 갈아 치우는 코드가 필요하기 때문에 단 한번만 실행되는 조건이 필요함.
    if count == 0:
        # count가 0일 때만 도는 코드
        hot_temp = max(temp)
        cold_temp = min(temp)
        got_sity = name
        cold_city = name
    else:
        # 계속 돌지 않고 else문 안에서만 돌것, 기준점은 서울로 했기 때문에 서로 비교만 되면 끝날 것.
        # 최저 온도가 cold_temp 보다 낮으면, cold_temp 에 값을 넣는다.
        if min(temp) < cold_temp:
            cold_temp = min(temp)
            cold_city = name

        #서울 끝나고 이제 대전값 도는중. 이 조건이 만족되면 name에 대전으로 갈아 치워지고 만족하지 못하면 서울 그대로.
        # 최고 온도가 hot_temp 보다 높으면, hot_tem 에 값을 새로 넣는다.
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
    count += 1

print(f'최고로 더웠던 지역은{hot_city}이고 온도{hot_temp}도 였고 최고로 추웠던 지역은 {cold_city}이고 온도{cold_temp}도 였다. ' )



# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
# = 서울 온도 리스트에 2가 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in city['서울']:
    print('네 있어요')
else:
    print('아니요 없어요')