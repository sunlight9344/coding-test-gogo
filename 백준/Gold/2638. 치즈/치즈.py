from collections import deque
import sys
import heapq
input = sys.stdin.readline

N,M = map(int,input().split())
pan = []
for _ in range(N):
    pan.append(list(map(int,input().split())))

visited = [[False for _ in range(M)]for _ in range(N)]
score = [[0 for _ in range(M)]for _ in range(N)]
heap = []
heapq.heappush(heap,(0,0,0))
visited[0][0] = True

dr = [0,1,0,-1]
dc = [1,0,-1,0]

ans = 0

while heap:
    time, r, c = heapq.heappop(heap)
    ans = max(time,ans)
    for k in range(4):
        next_r = r + dr[k]
        next_c = c + dc[k]

        if 0 <= next_r < N and 0 <= next_c < M:
            if not visited[next_r][next_c]:
                if pan[next_r][next_c] == 1:
                    if score[next_r][next_c] == 1:
                        heapq.heappush(heap,(time+1,next_r,next_c))
                        visited[next_r][next_c] = True
                    else:
                        score[next_r][next_c] += 1
                else:
                    heapq.heappush(heap,(time,next_r,next_c))
                    visited[next_r][next_c] = True

print(ans)