import sys
input = sys.stdin.readline

def dfs(node,now_cost):
    global ans

    if node == end:
        ans = now_cost
        return

    visited[node] = True

    for togo in connection[node]:
        if not visited[togo]:
            dfs(togo,now_cost + cost_data[node][togo])

N,M = map(int,input().split())
connection = [[]for _ in range(N+1)]
cost_data = [[0 for _ in range(N+1)]for _ in range(N+1)]


for _ in range(N-1):
    a,b,cost = map(int,input().split())
    connection[a].append(b)
    connection[b].append(a)
    cost_data[a][b] = cost
    cost_data[b][a] = cost

for _ in range(M):
    visited = [False]*(N+1)
    start,end = map(int,input().split())
    ans = 0
    dfs(start,0)
    print(ans)