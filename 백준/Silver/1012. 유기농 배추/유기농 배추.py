from collections import deque

def dfs(r,c):
    
    visited[r][c] = True
    for dr,dc in [[-1,0],[0,-1],[1,0],[0,1]]:
        nxt_r = r+dr
        nxt_c = c+dc

        if 0<=nxt_r<row and 0<=nxt_c<col:
            if data[nxt_r][nxt_c] and not visited[nxt_r][nxt_c]:
                visited[nxt_r][nxt_c]= True
                dfs(nxt_r,nxt_c)
               
for _ in range(int(input())):
    col,row,K = map(int,input().split())
    data = [[0]*col for _ in range(row)]
    visited = [[False]*col for _ in range(row)]
    
    for _ in range(K):
        c,r = map(int,input().split())
        data[r][c] = 1
        
    ans = 0
    for r in range(row):
        for c in range(col):
            if data[r][c] and not visited[r][c]:
                dfs(r,c)
                ans += 1
    print(ans)