n=input()
M=input().split()
Sum=0
for a in range(1,int(n)+1):
    Sum+=(a*int(M[a-1]))
print(Sum)
