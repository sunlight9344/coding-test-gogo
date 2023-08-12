N = int(input())

data = [0]*1000001
data[0],data[1],data[2],data[3],data[4] = 0,1,2,3,5

for i in range(5,N+1):
    data[i] = (data[i-1]%15746+data[i-2]%15746)%15746
print(data[N])