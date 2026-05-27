while True:
    try:
        time=range(0,60)
        print(time[25-int(input())])
    except EOFError:
        break