from collections import deque

def dfs(node):
    visited = [False]*(N+1)
    stack = [node]
    
    while stack:
        x = stack.pop()
        if not visited[x]:
            print(x,end=' ')
        visited[x] = True
        
        for togo in sorted(data[x],reverse=True):
            if not visited[togo]:
                stack.append(togo)
                
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

dfs(V)
print()
bfs(V)