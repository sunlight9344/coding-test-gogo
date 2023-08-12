N,K = map(int,input().split())

pack = [0 for _ in range(K+1)]
stuff = []
for _ in range(N):
    w,v = map(int,input().split())
    stuff.append((w,v))

for i in range(N):
    w,v = stuff[i]
    for j in range(K,0,-1):
        if j >= w:
            pack[j] = max(pack[j],pack[j-w]+v)
            
print(pack[K])