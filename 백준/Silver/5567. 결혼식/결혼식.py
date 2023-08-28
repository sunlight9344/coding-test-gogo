import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0
queue = deque([(1,0)])
visited = [False]*(N+1)
visited[1] = True
while queue:
    x, depth = queue.popleft()

    for togo in graph[x]:
        if not visited[togo] and depth <= 1:
            queue.append((togo,depth+1))
            ans += 1
            #print(togo)
            visited[togo] = True

print(ans)