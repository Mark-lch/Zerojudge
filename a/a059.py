import sys
data=list(map(int,sys.stdin.read().split()))
it=iter(data)
for b in range(1,next(it)+1):
    result=0
    start=next(it)
    end=next(it)
    scope=range(start,end+1)
    for a in range(int(pow(end,0.5))+1):
        outcome=a**2
        if outcome in scope:
            result+=outcome
    print(f"Case {b}: {result}")