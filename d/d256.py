#import math
import sys
data=list(map(int,sys.stdin.read().split()))
it=iter(data)

def main():
    N=next(it)
    for _ in range(N):
        GCD=next(it)
        LCM=next(it)
        
        if LCM%GCD==0:
            #judge(LCM//GCD,GCD)
            print(GCD,LCM)
        else:
            print(-1)
        #2 24 , 6 8 
        #24/2=12 3*4=12,2*6=12 12=2^2 *3
    
# def judge(tp,GCD):
#     factor=1
#     while factor*factor<=tp:
#         if tp%factor==0 and math.gcd(factor,tp//factor)==1:
#             print(GCD*factor,GCD*tp//factor)
#             return 
#         factor+=1
#    else:
#        print(-1)
main()

"""非常 白癡"""

#整人吧這題