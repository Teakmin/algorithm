N =  #컴퓨터 개수
M =  #연결쌍 개수

for _ in range(M):
    line = input().rstrip()
    if line[0] == '1':
        first_group.append(int(line[2:]))

