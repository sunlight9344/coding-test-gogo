N = int(input())

data = []
for _ in range(N):
    data.append(int(input()))
    
data.sort()
i = 1
ans = 0
for k in data:
    ans += abs(i-k)
    i+=1
print(ans)