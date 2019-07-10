# DOCstring (document)
"""
다음과 같은 내용의 파일 quest.txt 가 있다.
0
1
2
3

이 파일의 내용을 다음과 같이 역순으로 revers_quest.txt. 라는 파일로 저장하시오.
3
2
1
0
"""
# # 0. 만들어...
# with open('quest.txt', 'w') as f:
#     for i in range(4):
#         f.write(f'This is line {i+1}.\n')

# # 1. 읽고
# with open('quest.txt', 'r') as f:
#     lines = f.readlines

# # 2. 뒤집고
# lines.reverse()

# # 3. 작성하고
# with open('reverse_quest.txt', 'w') as f:
#     for line in lines:
#         f.write(line)

with open('quest.txt', 'w') as f:
    for i in range(0, 4):
        f.write(f'{i}\n')

with open('quest.txt', 'r') as f:
    lines = f.readlines()
    lines.reverse()
	
with open('reverse_quest.txt', 'w') as f:
    for line in lines:
        f.write(line)
        print(line)
