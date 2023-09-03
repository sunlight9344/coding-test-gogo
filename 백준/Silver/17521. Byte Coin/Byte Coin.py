import sys
input = sys.stdin.readline

N,W = map(int,input().split())
prices = []
for _ in range(N):
    prices.append(int(input()))

for i in range(N-1):
    if prices[i] < prices[i+1]:
        cnt = W // prices[i]
        W += cnt * (prices[i+1] - prices[i])
print(W)