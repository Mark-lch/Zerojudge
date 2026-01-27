import sys

def prime(c,n,r,N):
    if c>=N: 
        return True
    x=pow(c,n,N)
    if x==1 or x==N-1:
        return True
    else:
        for _ in range(r-1):
            x=pow(x,2,N)
            if x==N-1:
                return True
        return False

def Count():
    RESULT=[]
    witness=[2,7,61]
    data=list(map(int,sys.stdin.read().split()))
    if not data: return
    it=iter(data)
    
    while True:
        try:
            a=next(it)
            b=next(it)
            result=0
            for N in range(a,b+1):
                
                if N==1:continue
                if N==2 or N==3: 
                    result+=1
                    continue
                if N%2==0:continue
                n=N-1
                r=0
                while n%2==0:
                    n//=2
                    r+=1

                for c in witness:
                    receive=prime(c,n,r,N)
                    if receive:
                        continue
                    elif not receive:
                        break
                else:
                    result+=1
            RESULT.append(str(result))
        except StopIteration:
            sys.stdout.write('\n'.join(RESULT))
            break                                

Count()