# read() : 개행문자를 포함한 하나의 문자열 (통째로 읽어옴 : 단점 - 수정이 힘듦)
with open('with_ssafy.txt', 'r') as f:
    # 박스에 담기
   all_text = f.read()
   print(all_text)

# readlines() : 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list로 만들어냄 (read()의 단점 보완)
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
       print(line.strip())
        # print(dir(line))