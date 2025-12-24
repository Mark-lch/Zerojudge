while True:
    from datetime import date
    try:
        Data1=list(map(int,input().split()))
        Data2=list(map(int,input().split()))
        DAY1=date(Data1[0],Data1[1],Data1[2])
        DAY2=date(Data2[0],Data2[1],Data2[2])
        print(abs((DAY1-DAY2).days))
    except EOFError:
        break