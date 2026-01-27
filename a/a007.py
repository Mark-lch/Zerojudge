#import sys
#
#n=0
#data=[]
#data=list(map(int,sys.stdin.read().split()))
#
##for i in range(2,int(pow(data,0.5))+1):
##    if data%i==0:
##        print("非質數")
##        break
##    else:
##        print("質數")
#
#while n <len(data):
#    i=2
#    while i*i<=data[n]: #i<=pow(data,0.5)
#        if data[n]%i==0: 
#            data[n]="非質數"
#            break
#        i+=1
#    else:
#        data[n]="質數"
#    n+=1
#sys.stdout.write("\n".join(data))
"""...TLE..."""

"""
import sys
n=0

data=list(map(int,sys.stdin.read().split()))

limit=int(2147483647**0.5)+1

is_prime=[True]* (limit+1)

is_prime[0] = is_prime[1] = False

for p in range(2,limit+1):
    if is_prime[p]:
        is_prime[p*p:limit+1:p]=[False]*len(range(p*p,limit+1,p))

prime=[i for i,m in enumerate(is_prime) if m]

while n<len(data):
    for i in prime:
        if i*i>data[n]:
            data[n]="質數"
            break

        elif data[n]%i==0:
            data[n]="非質數"
            break
                
    else:
        data[n]="質數"
    n+=1

sys.stdout.write("\n".join(data))
"""

"""...TLE..."""

import sys

def examine():
    RS=[]
    wn=[2,7,61]
    data=sys.stdin.read().split()
    if not data:
        return
    
    data=list(map(int,data))
    
    for N in data:
        if N==1:
            RS.append("非質數")
            continue
        if N==2 or N==3:
            RS.append("質數")
            continue
        if N%2==0:
            RS.append("非質數")
            continue
        
        d=N-1
        r=0
        while d%2==0:
            d//=2
            r+=1

        is_prime=True

        

        for c in wn:
            if c>=N: break

            x=pow(c,d,N)

            if x==1 or x==N-1:
                continue
            
            for _ in range(r-1):
                x=pow(x,2,N)
                if  x==N-1:
                    break
            else:
                is_prime=False
                break
                            
        if is_prime:
            RS.append("質數")
        else:
            RS.append("非質數")
    sys.stdout.write("\n".join(RS))

examine()