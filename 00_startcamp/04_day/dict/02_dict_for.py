# 딕셔너리 반복문 활용하기

lunch = {
  '중국집': '02-0000-0000',
  '분식집': '031-123-1234',
  '일식집': '02-987-6543'
}

# 기본 활용
for key in lunch:
    print(key)
    print(lunch[key])


# .items() 한방에 뽑아올 수 있음 key, value는 바뀌어도 되지만 통상적으로 저렇게 씀.
for key, value in lunch.items():
    print(key, value)

# value 만 가져오기 .values()
for value in lunch.values():
    print(value)

# key 만 가져오기 .keys()
for key in lunch.keys():
    print(key)


