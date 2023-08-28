import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
from collections import deque
import math

N,K,M = map(int,input().split())

MAX_INDEX = N+M+1

graph = [[] for _ in range(MAX_INDEX)]
visited = [False]*(MAX_INDEX)

for i in range(1,M+1):
    arr = list(map(int,input().split()))
    
    for x in arr:
        graph[x].append(N+i)
        graph[N + i].append(x)

heap = deque([(0,1)])
found = False

while heap:
    cost,x = heap.popleft()
    if x == N:
        print(cost // 2 + 1)
        found = True
        break
    visited[x] = True

    for togo in graph[x]:
        if not visited[togo]:
            heap.append((cost+1,togo))
            visited[togo] = True

if not found:
    print(-1)