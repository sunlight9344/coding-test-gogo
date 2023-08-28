from collections import deque

a,b,A,B = map(int,input().split())

queue = deque([(0,0,0)])
visited = set([(0,0)])
found = False

while queue:
    now_a,now_b,score = queue.popleft()

    if now_a == A and now_b == B:
        ans = score
        found = True
        break

    # A 물통 채우기
    if (a,now_b) not in visited:
        queue.append((a,now_b,score+1))
        visited.add((a,now_b))

    # A 물통 버리기
    if (0,now_b) not in visited:
        queue.append((0,now_b,score+1))
        visited.add((0,now_b))

    # B 물통 채우기
    if (now_a,b) not in visited:
        queue.append((now_a,b,score+1))
        visited.add((now_a,b))

    # B 물통 버리기
    if (now_a,0) not in visited:
        queue.append((now_a,0,score+1))
        visited.add((now_a,0))

    # A -> B
    if now_a <= b-now_b:
        if (0,now_b+now_a) not in visited:
            queue.append((0,now_b+now_a,score+1))
            visited.add((0,now_b+now_a))
    else:
        left_b = b-now_b
        if (now_a-left_b,b) not in visited:
            queue.append((now_a-left_b,b,score+1))
            visited.add((now_a-left_b,b))

    # B -> A
    if now_b <= a-now_a:
        if (now_a+now_b,0) not in visited:
            queue.append((now_a+now_b,0,score+1))
            visited.add((now_a+now_b,0))
    else:
        left_a = a-now_a
        if (a,now_b-left_a) not in visited:
            queue.append((a,now_b-left_a,score+1))
            visited.add((a,now_b-left_a))

if found:
    print(ans)
else:
    print(-1)
