strg=list(input())
elist=[]
for i in strg:
   if i not in elist:
      elist.append(i)
if strg==elist:
   print("Yes")
else:
   print("No")
