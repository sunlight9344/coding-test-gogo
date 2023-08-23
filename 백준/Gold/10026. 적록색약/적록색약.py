import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,color,array):
    queue = deque([(x,y)])

    while queue:
        i,j = queue.popleft()
        visited[i][j] = True

        for d in range(4):
            nxt_i = i + di[d]
            nxt_j = j + dj[d]

            if 0 <= nxt_i < N and 0 <= nxt_j < N:
                if not visited[nxt_i][nxt_j] and array[nxt_i][nxt_j] == color:
                    queue.append((nxt_i,nxt_j))
                    visited[nxt_i][nxt_j] = True

di = [-1,0,1,0]
dj = [0,-1,0,1]

N = int(input())

array, array2 = [],[]
cnt,cnt2 = 0,0

for _ in range(N):
    str1 = input().rstrip()
    array.append(str1)

    temp = ""
    for ch in str1:
        if ch == 'R':
            temp += 'G'
            continue
        temp += ch
    array2.append(temp)

visited = [[False for _ in range(N)]for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j,array[i][j],array)
            cnt += 1


visited = [[False for _ in range(N)]for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j,array2[i][j],array2)
            cnt2 += 1

print(cnt,cnt2)