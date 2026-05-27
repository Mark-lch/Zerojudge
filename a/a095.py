while True:
    try:
        N,R=map(int,input().split())
        if N==R:print(R)
        else:print(R+1)
        
    except EOFError:
        break