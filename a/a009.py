password=input()
for a in range(len(password)):
    print(chr(ord(password[a])-7),end="")