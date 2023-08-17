str = input()

c = '7'
n = [0,0]
for s in str:
    if s != c:
        c = s
        n[(int)(s)] += 1
    
print(min(n))