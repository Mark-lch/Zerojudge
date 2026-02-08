N=int(input())
data=list(map(int,input().split()))
result=[0]*N
result[0]=data[0]

for n in range(1,N):
    result[n]=data[n]+result[n-1]

print(*result)  

#前綴和演算法