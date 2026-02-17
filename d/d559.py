while True:
    try:
        data=input()
        print(f"""'C' can use printf("%d",n); to show integer like {data}""")
    
    except EOFError:
        break