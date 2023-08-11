import sys
import heapq
input = sys.stdin.readline

N = int(input())

heap = []
for _ in range(N):
    heapq.heappush(heap,int(input()))

if len(heap)==1:
    print(0)
    exit(0)

result = 0
while True:
    a,b = heapq.heappop(heap),heapq.heappop(heap)
    result += a+b
    if not heap:
        break
    heapq.heappush(heap,a+b)
    
print(result)