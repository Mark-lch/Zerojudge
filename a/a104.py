while True:
    try:
        N=input()
        A=list(map(int,input().split()))
        A.sort()
        print(*A)
    except(EOFError):
        break