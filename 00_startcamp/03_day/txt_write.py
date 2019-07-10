# 1. 변수에 만들고 싶은 파일을 open() 해야 한다.
# open() 할때 r: 읽기 / w: 쓰기(+덮어씌워짐) / a: 추가
f = open('ssafy.txt', 'w')
for i in range(10):
    f.write(f'This is line {i+1}.\n')
        # n은 enter의 약자.\는 원래의 기능과 문자의 기능을 왔다갔다 해주는 듯
f.close()
# with 구문 (context manager)
with open('with_ssafy.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line {i+1}.\n')

# writelines() : list를 넣어주면, 요소 하나당 한 줄씩 작성한다.
with open('ssafy.txt', 'w') as f:
    # w는 덮어 씌우기의 의미여서 그대로 적용 시켜도 됨
    f.writelines(['0\n', '1\n', '2\n', '3\n'])

# 이스케이프 문자 (기존 문자의 능력을 탈출)
#\n : 개행문자(다음 줄 이동)
#\t : 탭문자(Tap)
#\\ : 백슬래쉬를 사용하기 위해 (출력 : \ )
#\' : 따옴표
#\" : 쌍따옴표