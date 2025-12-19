_=0
N=int(input())
while _<N:
    Time=list(map(int,input().split()))
    if (((Time[2]*60)+Time[3])-((Time[0]*60)+Time[1])-Time[-1])>=0:
        print("Yes")
    else:
        print("No")
    _+=1