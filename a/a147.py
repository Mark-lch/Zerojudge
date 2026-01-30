import sys
def pia():
    data=sys.stdin.read().split()
    it=iter(data)
    while True:
        try:
            N=int(next(it))
            for n in range(1,N):
                if (n%7)!=0:
                    print(n,end=" ")
            print()
        except StopIteration:
            break
pia()