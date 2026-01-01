import string
trans=str.maketrans(string.punctuation," "*len(string.punctuation))
while True:
    try:
        SP=input()
        RS=SP.translate(trans)
        print(len(RS.split()))
    except EOFError:
        break