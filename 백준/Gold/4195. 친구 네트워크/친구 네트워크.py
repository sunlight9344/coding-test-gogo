def find_parent(a):

    if dic[a] != a:
        dic[a] = find_parent(dic[a])
    return dic[a]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a == b:
        return
    
    dic[b] = a
    cnt[a] += cnt[b]
    
for _ in range(int(input())):
    dic = {}
    cnt = {}
    N = int(input())
    for _ in range(N):
        a,b = input().split()
        
        if a not in dic:
            dic[a] = a
            cnt[a] = 1
        if b not in dic:
            dic[b] = b
            cnt[b] = 1
        union(a,b)
        print(cnt[find_parent(a)])