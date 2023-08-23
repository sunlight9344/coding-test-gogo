for _ in range(int(input())):
    N = int(input())
    array = list(map(int,input().split()))
    array.sort()
    new_array = []
    ans = 0

    for i in range(0,N,+2):
        new_array.append(array[i])

    if N%2:
        for i in range(N-2,0,-2):
            new_array.append(array[i])
    else:
        for i in range(N-1,0,-2):
            new_array.append(array[i])

    #print(new_array)
    new_array.append(new_array[0])
    #print(new_array)

    for i in range(N-1):
        ans = max(ans,abs(new_array[i+1]-new_array[i]))
    
    print(ans)