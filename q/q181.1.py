import sys
data=list(map(int,sys.stdin.read().split()))
it=iter(data)

g=next(it)
r=next(it)
circle=g+r
result=0
for _ in range(next(it)):
    a=next(it)
    A=a%circle
    if A<g :
        continue
    
    result+=circle-A

print(result)