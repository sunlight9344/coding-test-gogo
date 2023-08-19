import heapq

N,K = map(int,input().split())

array = list(map(int,input().split()))

max_length = max(max(array),-min(array))

positive = []
negative = []

for k in array:
    if k > 0:
        heapq.heappush(positive,-k)
    else:
        heapq.heappush(negative,k)

result = 0

while positive:
    result += heapq.heappop(positive)
    for _ in range(K-1):
        if positive:
            heapq.heappop(positive)
            
while negative:
    result += heapq.heappop(negative)
    for _ in range(K-1):
        if negative:
            heapq.heappop(negative)

print(-result*2 - max_length)