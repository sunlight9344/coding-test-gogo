import heapq
import sys
from collections import deque

input = sys.stdin.readline

def dijkstra():
        
        dp[start] = 0
        heap = []
        heapq.heappush(heap,[0,start])
        
        while heap:
            cost,now = heapq.heappop(heap)
            if dp[now] < cost:
                continue
            
            for togo in data[now]:
                next_score = cost + togo[1]
                
                if next_score < dp[togo[0]] and not is_delete[now][togo[0]]:
                    dp[togo[0]] = next_score
                    heapq.heappush(heap,(next_score,togo[0]))
def bfs():
    queue = deque()
    queue.append(end)
    visited = [False] * N
    while queue:
        now = queue.popleft()
        
        if now == start:
            continue
        for prev,cost in data2[now]:
            if dp[prev]+cost == dp[now] and not is_delete[prev][now]:
                queue.append(prev)
                is_delete[prev][now] = True
                
while True:
    N,M = map(int,input().split())
    
    if N==0 and M==0:
        break
    
    data = [[]for _ in range(N)]
    data2 = [[]for _ in range(N)]
    
    start,end = map(int,input().split())
    
    for _ in range(M):
        a,b,s = map(int,input().split())
        data[a].append((b,s))
        data2[b].append((a,s))
        
    is_delete = [[False for _ in range(N)]for _ in range(N)]
    dp = [1e9]*N
    dijkstra()

    bfs()
    
    dp = [1e9]*N            
    dijkstra()

    if dp[end] == 1e9:
        print(-1)
    else:
        print(dp[end])
