co=input()
for n in range(len(co)//2):
    if co[n]!=co[-1-n]:
        print("no")
        break
else:
    print("yes")
    
###優雅解法:))###