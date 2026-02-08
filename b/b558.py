while True:
    try:
        N=int(input())
        n=1
        result=1
        while n<N:
            result+=n
            n+=1
        print(result)
        #1 2 4 7 11 16
    except EOFError:
        break