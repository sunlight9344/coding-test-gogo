from collections import deque
import math

a,b = map(int,input().split())

found = False
queue = deque([(a,0)])
ans = math.inf
while queue:
    x,cnt = queue.popleft()

    if x == b:
        ans = min(ans,cnt)
        found = True

    mul_x = x*2
    one_x = int(str(x)+"1")

    if mul_x <= b:
        queue.append((mul_x,cnt+1))

    if one_x <= b:
        queue.append((one_x,cnt+1))

if found:
    print(ans+1)
else:
    print(-1)