while True:
    try:
        a=0
        Ln,L=[],[]
        N=int(input())
        while a<N:
            L.append(int(input()))
           # if int(L[a])>0:
           #     Ln.append((len(L)))
           # else:
           #     Ln.append((-len(L)))
            a+=1
           # print(Ln)
        L.sort()
        for b in range(len(L)):
            print(L[b])
    except EOFError:
        break