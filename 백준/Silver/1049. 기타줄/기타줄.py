import math
N, M = map(int, input().split())

pack, sol = math.inf, math.inf
for _ in range(M):
    p, s = map(int, input().split())
    pack = min(pack, p)
    sol = min(sol, s)

ans = 0

while N > 0:

    if sol * 6 < pack:
        ans += sol * N
        break
    else:
        if sol * N < pack:
            ans += sol * N
            break
        else:
            ans += pack
            N -= 6

print(ans)
