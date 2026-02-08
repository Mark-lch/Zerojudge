import math
def LCM(a,b):
    rs=math.gcd(a,b)
    if not rs: return 0
    return abs(a)//rs*abs(b)
        
data=list(map(int,input().split()))

Mi=data[0]
Mx=data[1]
a=data[2]
b=data[3]
result=0
common=LCM(a,b)

if a:
    result+=abs((Mx//a)-((Mi-1)//a))

if b:
    result+=abs((Mx//b)-((Mi-1)//b))

if Mi<=0<=Mx and common==0 and a==b:
    result+=1

elif common:
    result-=abs((Mx//common)-((Mi-1)//common))

print(result)