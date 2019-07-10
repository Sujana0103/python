strg=input()
sarr=[]
for i in strg:
   if i.isnumeric():
      sarr.append(i)
print("".join(sarr))
