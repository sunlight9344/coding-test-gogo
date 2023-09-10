import sys
input = sys.stdin.readline

N = int(input())

array = []
for _ in range(N):
    array.append(int(input()))

array.sort(reverse=True)

max_value = array[0]
cnt = 1
for i in range(1,len(array)):
    if array[i] * (i+1) > max_value * cnt:
        max_value = array[i]
        cnt = i+1

print(max_value * cnt)