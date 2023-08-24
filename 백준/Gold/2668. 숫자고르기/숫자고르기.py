import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def cycle(x):

    visited[x] = True
    y = array[x]

    if not visited[y]:
        cycle(y)
    elif not finished[y]:
        cnt = 0
        while y != x:
            result.append(y)
            y = array[y]
            cnt += 1
        result.append(x)

    finished[x] = True

N = int(input())
array = [0]

for _ in range(N):
    array.append(int(input()))

visited = [False]*(N+1)
finished = [False]*(N+1)
result = []
for x in range(1,N+1):
    if not visited[x]:
        cycle(x)

print(len(result))
for k in sorted(result):
    print(k)