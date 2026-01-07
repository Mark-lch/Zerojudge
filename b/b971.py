N=list(map(int,input().split()))
if N[-1]>0:
    N[1]+=1
else:
    N[1]-=1
print(*range(N[0],N[1],N[-1]))