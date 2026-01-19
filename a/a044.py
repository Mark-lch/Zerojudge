RS,RS1=1,1
while True:
    try:
        tm=int(input())
        for N in range(1,tm+1):
            RS1+=RS
            RS+=N
        print(RS1)
        RS1,RS=1,1
    except EOFError:
        break