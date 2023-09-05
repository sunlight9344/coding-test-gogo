import sys
input = sys.stdin.readline

N = int(input())
array = []
max_value = 0
max_index = 0
for i in range(N):
    n = int(input())
    array.append(n)
    if n > max_value:
        max_value = n
        max_index = i

cnt = 0
for i in range(max_index, -1, -1):
    if array[i] == max_value:
        cnt += 1
        max_value -= 1
print(N-cnt)
