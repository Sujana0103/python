nop=int(input())
ger=[]
pow=0
for i in range (0,nop+1):
    pow=abs((2**i)-nop)
    ger.append(pow)
print(min(ger))
