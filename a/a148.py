import sys
data=sys.stdin.read().split()
it=iter(data)
while True:
    try:
        N=int(next(it))
        result=0
        for _ in range(N):
            result+=int(next(it))
        if result/N >59: print("no")
        else: print("yes")
    except StopIteration:
        break