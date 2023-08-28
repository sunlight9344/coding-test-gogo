import sys
from collections import deque

input = sys.stdin.readline

a,b = map(int,input().split())

if a == b:
    print(0)
    exit(0)

visited = set([a])

queue = deque([(a,"")])
found = False

while queue:
    x,oper = queue.popleft()

    if x > int(1e9):
        continue
    
    if x == b:
        ans = oper
        found = True
        break

    for k in ["*","+","-","/"]:
        if k == "*":
            next_value = x * x
        elif k == "+":
            next_value = x + x
        elif k == "-":
            next_value = x - x
        else:
            next_value = 1
        if next_value not in visited:
            queue.append((next_value,oper+k))
            visited.add(next_value)

if found:
    print(ans)
else:
    print(-1)