row = input()
col = input()

dp = [[0]*(len(col)+1) for _ in range(len(row)+1)]

for r in range(1,len(row)+1):
    for c in range(1,len(col)+1):
        if row[r-1] == col[c-1]:
            dp[r][c] = dp[r-1][c-1]+1
        else:
            dp[r][c] = max(dp[r-1][c],dp[r][c-1])
print(dp[len(row)][len(col)])
