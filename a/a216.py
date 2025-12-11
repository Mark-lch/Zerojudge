while True:
    try:
        n=int(input())
        f,g=0,0
        for a in range(n):
            f=f+a+1
            g=g+f
        print(f,g)
    except(EOFError):
        break