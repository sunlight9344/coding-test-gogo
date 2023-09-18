import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    data = []
    ans = "YES"
    for _ in range(N):
        data.append(input().rstrip())
    data.sort()
    for i in range(N-1):
        index = len(data[i])
        if data[i] == data[i+1][:index]:
            ans = "NO"
            break

    print(ans)

