amount=int(input())
if amount>=40:
    print(100)
elif amount>20:
    print((amount-20)+(10*2)+60)
elif amount>10:
    print(((amount-10)*2)+60)
else:
    print(6*amount)