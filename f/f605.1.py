import sys
data=sys.stdin.read().split()
it=iter(data)

N=int(next(it))
diff=int(next(it))
Outcome=0
Total=0

for _ in range(N):
    result=0
    Max=0
    Min=999
    for _ in range(3):
        price=int(next(it))
        result+=price
        Max=max(Max,price)
        Min=min(Min,price)

    if Max-Min>=diff:
        Total+=(result//3)
        Outcome+=1

print(Outcome,Total)