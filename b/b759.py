from collections import deque
data=deque(input())
print("".join(data))

for _ in range(len(data)-1):
    data.append(data.popleft())
    print("".join(data))
    
    # for a in data:
    #     print(a,end="")
    # print()
    #for比較慢且大