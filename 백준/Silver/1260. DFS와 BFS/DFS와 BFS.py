from collections import deque

def dfs(node):
    print(node,end=' ')
    visited[node] = True
    for togo in sorted(data[node]):
        if not visited[togo]:
            dfs(togo)
            
def bfs(node):
    visited = [False]*(N+1)
    queue = deque([node])
    
    while queue:
        x = queue.popleft()
        if not visited[x]:
            print(x,end=' ')
        visited[x] = True
        
        for togo in sorted(data[x]):
            if not visited[togo]:
                queue.append(togo)


N,M,V = map(int,input().split())

data = [[]for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

stack = [V]
visited = [False]*(N+1)
dfs(V)

print()
bfs(V)