import sys
input = sys.stdin.readline
import heapq

N = int(input())

pan = []

for _ in range(N):
    pan.append(input())

heap = []
heapq.heappush(heap,(0,0,0))
visited = set([(0,0)])
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ans = 0

while heap:
    black,x,y = heapq.heappop(heap)
    if x == N-1 and y == N-1:
        ans = black
        break

    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]

        if 0 <= next_x < N and 0 <= next_y < N:
            if (next_x,next_y) not in visited:
                if pan[next_x][next_y] == '0':
                    heapq.heappush(heap,(black+1,next_x,next_y))
                else:
                    heapq.heappush(heap,(black,next_x,next_y))
                visited.add((next_x, next_y))

print(ans)