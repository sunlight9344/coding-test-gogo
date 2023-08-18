import heapq

N = int(input())
K = int(input())

loc = list(map(int,input().split()))

loc.sort()
heap = []
total_len = loc[-1]-loc[0]

for i in range(1,N):
    heapq.heappush(heap,-(loc[i]-loc[i-1]))

for k in range(K-1):
    if heap:
        total_len -= -heapq.heappop(heap)
    else:
        break
    
print(total_len)