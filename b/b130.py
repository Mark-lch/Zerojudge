input()
data=sorted(set(map(int,input().split())))
print(len(data),end="\n")
print(" ".join(list(map(str,data))))