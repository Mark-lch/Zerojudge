N=int(input())
LList=[]
d=2
while d*d<=N:
    while N%d==0:
        N=N//d
        LList.append(d)
    d+=1
if N>1:
     LList.append(N)

if len(LList)==1:
    print(LList[0])
else:
    LL=sorted(list(set(LList)))
    for c in range(len(LL)):
        if LList.count(LL[c])>1:
            LL[c]=f"{LL[c]}^{LList.count(LL[c])}"

    print(" * ".join(str(a) for a in LL))


"""一開始寫的錯誤的"""
#while N!=1:
#    for a in range(N):
#        while N%(a+1)==0 and a+1!=1:
#            N=N//(a+1)
#            LList.append(a+1)
#        if N==1:
#            break

#if len(LList)==1:
#    print(LList[0])
#elif len(LList)==2 and LList[0]!=LList[1]:
#    print(LList[0],"*",LList[1])
#else:
#    LList.sort()
#    LL=list(set(LList))
#    for b in range(len(LL)):
#        if LList.count(LL[b])!=1:
#            print(f"{LL[b]}^{LList.count(LL[b])} *",end=" ")
#        else:
#            print(LL[b],end=" ")