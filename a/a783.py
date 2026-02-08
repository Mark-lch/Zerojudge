import sys
data=list(map(int,sys.stdin.read().split()))
it=iter(data)
Result=[]

def GCD(a,b):
    if not b: return str(a)
    return GCD(b,a%b)
    
while True:
    try:
        a=next(it)
        b=next(it)

        Result.append(GCD(a,b))
    except StopIteration:
        sys.stdout.write("\n".join(Result))
        break