import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int,input().split()))

dp = [data[0]]

for i in range(1,N):
    
    if data[i] > dp[-1]:
        dp.append(data[i])
    else:
        left = 0
        right = len(dp)
        
        while left<right:
            mid = (left+right)//2
            if dp[mid] < data[i]:
                left = mid+1
            else:
                right = mid
        dp[right] = data[i]
        

print(len(dp))