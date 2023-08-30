N = int(input())
array = list(map(int,input().split()))

day = 1

array.sort(reverse=True)

for i in range(len(array)):
    day = max(day,array[i]+i+1)
print(day+1)