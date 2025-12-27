while True:
    Mon=[31,28,31,30,31,30,31,31,30,31,30,31]
    try:
        M,D=map(int,input().split())
        m,d=map(int,input().split())
        for n in range(M-1):
            D+=Mon[n]
        for N in range(m-1):
            d+=Mon[N]
        rs=d-D
        if (rs)>=0:
            print(rs)
        else:
            print(365+rs)
    except EOFError:
        break
