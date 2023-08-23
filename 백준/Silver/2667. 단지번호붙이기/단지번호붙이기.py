import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,cnt):
    queue = deque([(x,y)])
    how_called[cnt] += 1
    while queue:
        i,j = queue.popleft()
        visited[i][j] = True
        for k in range(4):
            next_i = i + di[k]
            next_j = j + dj[k]
            if 0 <= next_i < N and 0 <= next_j < N:
                if array[next_i][next_j] == '1' and not visited[next_i][next_j]:
                    queue.append((next_i,next_j))
                    visited[next_i][next_j] = True
                    how_called[cnt] += 1

N = int(input())

visited = [[False for _ in range(N+1)]for _ in range(N+1)]
array = []
how_called = [0] * 630
di = [-1,0,1,0]
dj = [0,1,0,-1]

for i in range(N):
    array.append(input())

cnt = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == '1' and not visited[i][j]:
            bfs(i,j,cnt)
            cnt += 1
print(cnt)
how_called.sort()
for called in how_called:
    if called:
        print(called)