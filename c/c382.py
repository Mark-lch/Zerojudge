formula=input()

if int(formula.find("+"))!=-1:
    operator=formula.find("+")
    print(int(formula[:operator])+int(formula[operator+1:]))
elif int(formula.find("-"))!=-1:
    operator=formula.find("-")
    print(int(formula[:operator])-int(formula[operator+1:] ))
elif int(formula.find("*"))!=-1:
    operator=formula.find("*")
    print(int(formula[:operator])*int(formula[operator+1:] ))
else:
    operator=formula.find("/")
    print(int(formula[:operator])//int(formula[operator+1:] ))