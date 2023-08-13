N,start_vol,max_vol = map(int,input().split())
v = list(map(int,input().split()))

dp = [False] * (max_vol+1)
dp[start_vol] = True

for vol in v:
    new_dp = [False] * (max_vol+1)
    for i in range(max_vol+1):
        if dp[i]==True:
            if 0 <= i-vol <= max_vol:
                new_dp[i-vol] = True
            
            if 0 <= i+vol <= max_vol:
                new_dp[i+vol] = True
    dp = new_dp

result = -1
for i in range(max_vol,-1,-1):
    if dp[i] == True:
        result = i
        break
        
print(result)