import sys
input = sys.stdin.readline

def sumStr(str):
    s = 0
    for ch in str:
        if ch.isdigit():
            s += int(ch)
    return s
            
N = int(input())
array = []
for _ in range(N):
    array.append(input().rstrip())

array.sort(key = lambda x:(len(x),sumStr(x),x))

for ar in array:
    print(ar)