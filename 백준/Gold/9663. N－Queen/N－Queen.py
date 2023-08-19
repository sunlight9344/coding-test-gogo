def N_Queen(row_now,c_list):
    global ans
    #print(c_list)
    if row_now == N:
        #print(c_list)
        ans += 1
        return
    
    for c_now in range(N):
        if c_now not in c_list:
            kkk = True
            for row_pre in range(len(c_list)):
                if abs(row_now-row_pre) == abs(c_now-c_list[row_pre]):
                    #print(row_now,row_pre,c_now,c_list[row_pre])
                    kkk = False
                    break
            if kkk:
                N_Queen(row_now+1,c_list+[c_now])
    
    
N = int(input())
ans = 0
N_Queen(0,[])
print(ans)