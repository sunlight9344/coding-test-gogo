from bisect import bisect_right,bisect_left
import sys

input = sys.stdin.readline

N = int(input())

data = list(map(int,input().split()))

array = []
dp = []

for k in data:
    
    if not array or k > array[-1]:
        array.append(k)
        dp.append((len(array)-1,k))
        
    else:
        index = bisect_left(array,k)
        array[index] = k
        dp.append((index,k))
        
ans = []
L = len(array)-1

for k in reversed(dp):
    if k[0] == L:
        ans.append(k[1])
        L -= 1
print(len(array))
[print(i,end=' ') for i in reversed(ans)]
