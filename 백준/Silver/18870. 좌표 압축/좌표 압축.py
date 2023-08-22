N = int(input())
array = list(map(int,input().split()))

new_array = sorted(array)
data = {}
cnt = 0
max_value = 0

for k in new_array:
    if k not in data:
        data[k] = cnt
        cnt += 1
for k in array:
    print(data[k],end=' ')