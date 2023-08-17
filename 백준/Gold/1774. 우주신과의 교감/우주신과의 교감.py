import math

def find_parent(x):
    if data[x] != x:
        data[x] = find_parent(data[x])
    return data[x]

def union(a,b):
    
    a = find_parent(a)
    b = find_parent(b)
    
    if a==b:
        return
    
    if a < b:
        data[a] = data[b]
    else:
        data[b] = data[a]

N,M = map(int,input().split())

location = [0]
#cost = [[0 for _ in range(N+1)]for _ in range(N+1)]
array = []
data = [i for i in range(N+1)]

for i in range(N):
    location.append(tuple(map(int,input().split())))
    
for j in range(M):
    a,b = map(int,input().split())
    union(a,b)

for i in range(1,N+1):
    xi, yi = location[i][0], location[i][1]
    for j in range(i+1,N+1):
        xj, yj = location[j][0], location[j][1]
        #cost[i][j] = math.sqrt(abs(xi-xj)**2 + abs(yi-yj)**2)
        array.append((math.sqrt(abs(xi-xj)**2 + abs(yi-yj)**2),i,j))

array.sort()
ans = 0
for cost,start,end in array:
    if find_parent(start) != find_parent(end):
        union(start,end)
        ans += cost
print("%.2f"%round(ans,2))
