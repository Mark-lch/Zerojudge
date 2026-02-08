import sys 
data=list(map(int,sys.stdin.read().split()))
it=iter(data)

next(it)
while True:
    try:
        result=100-abs(next(it)+next(it))

        if 60<result<100: print("Happyyummy")
        elif 30<result<=60: print("hmm~~")
        elif 0<result<=30: print("sad!")
        else: print("evil!!")

    except StopIteration:
        break