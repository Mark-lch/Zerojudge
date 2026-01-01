while True:
    try:
        a,b=map(int,input().split())
        print(max(a,b)-min(a,b))
    except EOFError:
        break