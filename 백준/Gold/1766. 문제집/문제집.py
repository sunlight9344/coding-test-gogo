import heapq
import sys

## change
input = sys.stdin.readline

N,M = map(int,input().split())

data = [[]for _ in range(N+1)]
how_in = [0]*(N+1)
heap = []

for _ in range(M):
    a,b = map(int,input().split())
    data[a].append(b)
    how_in[b] += 1
    
for i in range(1,N+1):
    if how_in[i] == 0:
        heapq.heappush(heap,i)

ans = []
while heap:
    k = heapq.heappop(heap)
    ans.append(k)
    for to_visit in data[k]:
        how_in[to_visit] -= 1
        if not how_in[to_visit]:
            heapq.heappush(heap,to_visit)

for a in ans:
    print(a,end=' ')
    