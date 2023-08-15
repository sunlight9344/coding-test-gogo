import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int,input().split()))

dp = [1]*N
ans = [[i] for i in data]

for i in range(N):
    
    for j in range(i):
        if data[i] > data[j]:
            if dp[j]+1 > dp[i]:
                ans[i] = ans[j]+[data[i]]
            dp[i] = max(dp[i],dp[j]+1)
            
max_value = max(dp)
k = dp.index(max_value)      
print(max_value)
[print(i,end=' ') for i in ans[k]]