import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())

gems = []
bags = []

for _ in range(N):
    weight, price = map(int, input().split())
    gems.append((weight, price))

for _ in range(K):
    bags.append(int(input()))

gems.sort()
bags.sort()

heap = []
cur = 0
ans = 0

for bag in bags:

    while cur < N:
        weight, price = gems[cur]

        if bag >= weight:
            heapq.heappush(heap,-price)
            cur += 1
        else:
            break
    if heap:
        ans += heapq.heappop(heap)
print(-ans)