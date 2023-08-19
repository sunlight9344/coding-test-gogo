import heapq

N = int(input())

array = []

for _ in range(N):
    array.append(list(map(int,input().split())))

array.sort()

heap = []

for deadline,cup in array:
    heapq.heappush(heap,cup)
    
    if len(heap) > deadline:
        heapq.heappop(heap)
        
print(sum(heap))