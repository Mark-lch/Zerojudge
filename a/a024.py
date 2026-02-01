def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

data=input().split()
a=int(data[0])
b=int(data[-1])

print(gcd(a,b))

#遞迴可愛