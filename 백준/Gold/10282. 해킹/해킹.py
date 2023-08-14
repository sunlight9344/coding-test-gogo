import heapq
import math
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n,d,start_node = map(int,input().split())
    data = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        data[b].append([a,s])
    
    dp = [math.inf]*(n+1)
    dp[start_node] = 0
    heap = [[0,start_node]]
    while heap:
        cost,node = heapq.heappop(heap)
        for togo,s in data[node]:
            if cost+s < dp[togo]:          
                dp[togo] = cost+s
                heapq.heappush(heap,[cost+s,togo])
    max_value = 0
    max_count = 0
    for value in dp:
        if value != math.inf:
            max_count += 1
            if value > max_value:
                max_value = value
    print(max_count,max_value)
        