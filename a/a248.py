#此解NA,應該是float精度不足
#while True:
#    try:
#        from math import floor
#        a,b,N=map(int,input().split())
#        print(f"{(floor(a/b*10**N)/10**N):.{N}f}")
#    except EOFError:
#        break


#第一種AC解
from decimal import Decimal, ROUND_DOWN,getcontext
getcontext().prec=10000
while True:
    try:
        a,b,N=map(Decimal,input().split()) 
        print((a/b).quantize(Decimal(f"1E-{N}"),ROUND_DOWN))
    except EOFError:
        break


#AC解第二個
import sys
sys.set_int_max_str_digits(0)
while True:
    try:
        a,b,N=map(int,input().split()) 
        print((str(a//b)+f".{(((a%b)*10**N)//b):0{N}d}"))
    except EOFError:
        break