N, L = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

end = 0
ans = 0
for i in data:
    if i > end:
        end = i + L - 0.5
        ans += 1
print(ans)