import sys
data=list(map(int,sys.stdin.read().split()))
it=iter(data)
next(it)

def filter():
    result=[]
    Case=1
    while True:
        try:
            All=[]
            for _ in range(3):
                All.append(next(it))
            All.sort()
            result.append(f"Case {Case}: {All[1]}")
            Case+=1
        except StopIteration:
            sys.stdout.write("\n".join(result))
            break

filter()            