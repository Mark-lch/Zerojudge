data=input().split()
a=int(data[0])
b=int(data[-1])
if data[1]=="+":
    print(a+b)
elif data[1]=="-":
    print(a-b)
elif data[1]=="*":
    print(a*b)
else: print(a//b)