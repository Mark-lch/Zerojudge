data=input().split()
result=0
for y in range(int(data[0]),int(data[1])+1):
    if y%400==0: result+=1
    elif y%4==0 and y%100!=0:
        result+=1
print(result)