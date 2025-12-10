for t in range(int(input())):
    a,b,c,d=(int(x) for x in input().split())
    if b-a==d-c:
        print(a,b,c,d,d+(b-a))
    else:
        print(a,b,c,d,d*(b//a))