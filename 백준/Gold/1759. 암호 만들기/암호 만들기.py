def dfs(x,str):
    #print(str)
    if len(str) == L:
        cnt = 0
        for ch in str:
            if ch in moum:
                cnt += 1
        if cnt >= 1 and len(str)-cnt >=2:
            print(str)
        return
            
    for i in range(x,C):
        dfs(i+1,str+array[i])
        
L,C = map(int,input().split())
array = list(input().split())
array.sort()

moum = 'aeiou'

dfs(0,"")