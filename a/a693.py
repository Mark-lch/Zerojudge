import sys

def EAT():
    data=map(int,sys.stdin.read().split())
    it=iter(data)
    Result=[]
    while True:
        try:
            n=next(it)
            m=next(it)
            current=0
            S=[0]*(n+1)
            for a in range(1,n+1):
                current+=next(it)
                S[a]=current
            
            while m>0:
                result=0

                l=next(it)
                r=next(it)

                result=S[r]-S[l-1]
                #result=sum(Foods[next(it)-1:next(it)])

                # for a in range(next(it)-1,next(it)):
                #     result+=Foods[a]
                
                Result.append(str(result))
                m-=1

        except StopIteration:
            sys.stdout.write("\n".join(Result))
            break

EAT()