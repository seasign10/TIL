# 1. 읽고
with open('quest.txt', 'r') as f:
    lines = f.readlines()

# 2. 뒤집고
lines.reverse()

# 3. 작성하고
with open('reverse_quest.txt', 'w') as f:
    for line in lines:
        f.write(line)

with open('reverse_quest.txt', 'w') as f:
    f.writelines(lines)