while True:
    try:
        rs=0
        N=1
        point=int(input())
        while N<=point:
            for a in range(N,N+N+1):#12 234 3456 45678
                rs+=(a)
            N+=1
        print(rs)
    except EOFError:
        break