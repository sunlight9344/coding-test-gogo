from collections import deque

def bfs(node):
    visited = [False]*(N+1)
    count = 0
    queue = deque([node])
    
    while queue:
        x = queue.popleft()
        visited[x] = True
        for togo in data[x]:
            if not visited[togo]:
                count += 1
                visited[togo] = True
                queue.append(togo)
    return count

N,M = map(int,input().split())

data = [[]for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    data[b].append(a)

max_value = 0
res = []
for i in range(1,N+1):
    c = bfs(i)
    if c > max_value:
        max_value = c
        res = [i]
    elif c == max_value:
        res.append(i)

[print(i,end=" ") for i in sorted(res)]
        