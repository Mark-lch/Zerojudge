while True:
    try:
        RS,T=[],[]
        T=int(input())
        if T==0:
            print(T)
        while T:
            RS.append(T%2)
            T//=2
        while RS:
            print(RS.pop(),end="")
        print()
    except EOFError:
        break
                

#0 1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111
#0 1 2  3  4   5   6   7   8    9    10   11   12   13   14   15