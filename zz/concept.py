def gen():
    yield 1
print(next(gen()))


a,b,c= [int(x) for x in input().split()]#list comprehension, "a244.py"的另一寫法   

result=map(int, input().split()) 
print(list(result))
