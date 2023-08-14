def dfs(node):
    global ans
    
    for k in data[node]:
        if not visited[k]:
            visited[k] = True
            ans += 1
            dfs(k)
            
N = int(input())
K = int(input())

data = [[]for _ in range(N+1)]
for _ in range(K):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
    
visited = [False]*(N+1)
visited[1] = True
ans = 0
dfs(1)
print(ans)
