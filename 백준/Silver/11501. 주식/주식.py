for _ in range(int(input())):
    N = int(input())
    array = list(map(int,input().split()))

    max_value = 0
    max_array = [0]*N

    for k in range(N-1,-1,-1):
        max_value = max(max_value,array[k])
        max_array[k] = max_value

    ans = 0
    for k in range(N):
        ans += max_array[k] - array[k]
        
    print(ans)