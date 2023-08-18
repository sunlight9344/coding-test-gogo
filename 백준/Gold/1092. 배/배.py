N = int(input())
machines = list(map(int,input().split()))
M = int(input())
boxes = list(map(int,input().split()))

if max(boxes) > max(machines):
    print(-1)
    exit(0)

count = 0
ans = 0
visited = [False]*M
position = [0]*N
boxes.sort(reverse=True)
machines.sort(reverse=True)

while True:
    
    if count == M:
        break
    
    for i in range(N):
        while position[i] < len(boxes):
            if not visited[position[i]] and machines[i] >= boxes[position[i]]:
                visited[position[i]] = True
                position[i] += 1
                count += 1
                break
            position[i] += 1
    ans += 1

print(ans)