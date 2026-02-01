input()
data=list(map(int,input().split()))
result=1
count=1
for n in range(0,len(data)-1):
    if data[n]>data[n+1]:
        count+=1
    elif count>result:
        result=count
        count=1
    else: count=1
    # else:
    #     result=max(result,count)
if count>result:
    result= count 
#result=max(result,count)
print(result)

#為精簡寫法