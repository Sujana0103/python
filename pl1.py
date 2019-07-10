def longest(strg1,strg2):
        if(strg1 in strg2):
            return strg1
        else:
            return longest(strg1[0:len(strg1)-1],strg2)
intg = int(input())
x1= []
for _ in range(0,intg):
    x1.append(input())
x1.sort()
print(longest(x1[0],x1[intg-1]))
