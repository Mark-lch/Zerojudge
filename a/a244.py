for a in range(int(input())):
    M=input().split()
    if int(M[0])==1:
        print(int(M[1])+int(M[2]))
    elif int(M[0])==2:
        print(int(M[1])-int(M[2]))
    elif int(M[0])==3:
        print(int(M[1])*int(M[2]))
    elif int(M[0])==4:
        print(int(M[1])//int(M[2]))