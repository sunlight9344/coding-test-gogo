k = 1000 - int(input())

array = [500,100,50,10,5,1]

ans = 0
index = 0

while k:
    n = k // array[index]
    ans += n
    k %= array[index]
    index += 1
print(ans)