while True:
    try:
        a,b=map(int,input().split())
        if (a,b)==(-1,-1):
            break
        RS1=range(100)[(min(a,b)-max(a,b))]
        RS2=range(100)[(max(a,b)-min(a,b))]
        print(min(RS1,RS2))
    except EOFError:
        break