import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    k = int(input())
    
    if k:
        heapq.heappush(heap,k)
    else:
        if heap:
            x = heapq.heappop(heap)
            print(x)
        else:
            print(0)
    