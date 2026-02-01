import sys

def EAT():
    data=map(int,sys.stdin.read().split())
    it=iter(data)
    Foods=[]
    Result=[]
    while True:
        try:
            n=next(it)
            m=next(it)
                        
            for _ in range(n):
                Foods.append(next(it))
            
            while m>0:
                result=0
                for a in range(next(it)-1,next(it)):
                    result+=Foods[a]
                
                Result.append(str(result))
                m-=1

        except StopIteration:
            sys.stdout.write("\n".join(Result))
            break

EAT()