#from math import floor

#a,b,N=map(int,input().split())
#print(f"{(floor(a/b*10**N)/10**N):.{N}f}")

#from decimal import Decimal, ROUND_DOWN,getcontext
#a,b,N=map(Decimal,input().split()) 
#getcontext().prec=11000
#print((a/b).quantize(Decimal(f"1E-{N}"),ROUND_DOWN))

from decimal import Decimal, ROUND_DOWN,getcontext
getcontext().prec=10000
while True:
    try:
        a,b,N=map(Decimal,input().split()) 
        print((a/b).quantize(Decimal(f"1E-{N}"),ROUND_DOWN))
    except EOFError:
        break