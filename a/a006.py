a,b,c=(int(x) for x in input().split())
judge=(b**2)-(4*a*c)
if judge>0:
    print(f"Two different roots x1={int((-b+(judge)**0.5)//(2*a))} , x2={int((-b-(judge)**0.5)//(2*a))}")
elif judge==0:
    print(f"Two same roots x={-b//(2*a)}")
else:
    print("No real root")