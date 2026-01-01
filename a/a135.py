lang={"HELLO":"ENGLISH","HOLA":"SPANISH","HALLO":"GERMAN","BONJOUR":"FRENCH","CIAO":"ITALIAN","ZDRAVSTVUJTE":"RUSSIAN"}
N=0
while True:
    try:
        N+=1
        fr=input()
        if fr=="#":
            break
        rs=lang.get(fr,"UNKNOWN")
        print(f"Case {N}: {rs}")
    except EOFError:
        break