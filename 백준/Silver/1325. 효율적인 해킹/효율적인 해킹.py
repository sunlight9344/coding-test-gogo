def dfs(node):
    
    k = 0
    visited = [False]*(N+1)
    stack = [i]
    
    while stack:
        x = stack.pop()
        visited[x] = True
        
        for togo in data[x]:
            if not visited[togo]:
                k += 1
                visited[togo] = True
                stack.append(togo)
    return k

N,M = map(int,input().split())

data = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    data[b].append(a)

max_value = 0
res = []
for i in range(1,N+1):
    k = dfs(i)
    if k > max_value:
        res = [i]
        max_value = k
    elif k == max_value:
        res.append(i)

[print(i,end=' ') for i in sorted(res)]
    
