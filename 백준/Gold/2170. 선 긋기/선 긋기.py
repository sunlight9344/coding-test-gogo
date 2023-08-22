import sys
import math
input = sys.stdin.readline

N = int(input())

array = []
for _ in range(N):
    array.append(tuple(map(int,input().split())))

array.sort()

start,end = -math.inf,-math.inf
result = 0

for a,b in array:
    
    if start==a and b>end:
        result += b-end
        end = b
    elif start < a < end and end < b:
        result += b-end
        end = b
    elif a >= end: 
        result += b-a
        start = a
        end = b

print(result)
