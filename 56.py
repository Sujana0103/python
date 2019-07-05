strg=input()
for i in range(0,len(strg)):
   if(strg[i].isalpha() and strg[i].isdigit()):
    print("No")
else:
  print("Yes")
