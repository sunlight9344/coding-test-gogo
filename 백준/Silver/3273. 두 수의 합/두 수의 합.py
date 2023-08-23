N = int(input())
array = list(map(int,input().split()))
x = int(input())

array.sort()

start,end = 0, N-1
temp_sum = 0
ans = 0

while start < end:
    temp_sum = array[start] + array[end]
    if temp_sum < x:
        start += 1
    elif temp_sum > x:
        end -= 1
    else:
        ans += 1
        start += 1

print(ans)