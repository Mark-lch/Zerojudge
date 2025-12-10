while True:
    try:
        Y=int(input())

        if Y%400==0:
            print("閏年")
        elif Y%4==0 and Y%100!=0:
            print("閏年")
        else:
            print("平年")
    except(EOFError):
        break