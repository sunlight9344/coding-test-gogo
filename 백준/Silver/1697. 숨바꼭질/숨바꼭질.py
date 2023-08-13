from collections import deque

N,K = map(int,input().split())

def bfs(start_node):
    visited = [False]*100001
    
    queue = deque([[start_node,0]])

    while queue:
        x,depth = queue.popleft()

        if x == K:
            print(depth)
            break
        visited[x] = True
        for togo in [x-1,x+1,x*2]:
            if 0<=togo<=100000 and not visited[togo]:
                queue.append([togo,depth+1])
bfs(N)