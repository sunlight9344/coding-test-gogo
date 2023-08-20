def bfs(row,col):
    global ans
    
    q = set()
    q.add((row,col,pan[row][col]))
    
    while q:
        r,c,step = q.pop()
        ans = max(len(step),ans)
        
        for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            next_r = r+dr
            next_c = c+dc
            
            if 0<=next_r<R and 0<=next_c<C and pan[next_r][next_c] not in step:
                q.add((next_r,next_c,step+pan[next_r][next_c]))

        
R,C = map(int,input().split())

pan = []

for _ in range(R):
    pan.append(input())

ans = 0
bfs(0,0)
print(ans)