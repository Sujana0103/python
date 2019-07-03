strg=input()
count=0
for i in range(len(strg)):
  if(strg[i].isdigit()):
    count+=1
print(count)
