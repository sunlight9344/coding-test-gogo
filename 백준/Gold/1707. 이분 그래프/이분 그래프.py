import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def dfs(node,color):

    stack = [(node,color)]
    
    while stack:
        now_node,now_color = stack.pop()
        #print("node",now_node,"color",now_color)
        visited[now_node] = True
        for togo in graph[now_node]:
            if not visited[togo]:
                visited[togo] = True
                colors[togo] = now_color * -1
                stack.append((togo,now_color* -1))
            else:
                if colors[togo] != now_color * -1:
                    # print("stack",stack)
                    # print("visited",visited)
                    # print("togo",togo,"color",colors[togo])
                    return False
    return True

for _ in range(int(input())):
    N,E = map(int,input().split())
    visited = [False]*(N+1)
    colors = [1]*(N+1)
    graph = [[]for _ in range(N+1)]

    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1,N+1):
        ans = True
        if not visited[i]:
            if not dfs(i,1):
                ans = False
                break
        
    if ans:
        print("YES")
    else:
        print("NO")