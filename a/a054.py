NUM=input()
RS=0
dic = {
    'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14',
    'F':'15', 'G':'16', 'H':'17', 'I':'34', 'J':'18',
    'K':'19', 'L':'20', 'M':'21', 'N':'22', 'O':'35',
    'P':'23', 'Q':'24', 'R':'25', 'S':'26', 'T':'27',
    'U':'28', 'V':'29', 'W':'32', 'X':'30', 'Y':'31',
    'Z':'33'
    }
for n in range(9): 
    RS+=(8-n)*int(NUM[n])
for key,value in dic.items():
    if int((str(10-((9*int(value[-1])+int(value[0])+RS)%10)))[-1])==int(NUM[-1]):
        print(key,end="")