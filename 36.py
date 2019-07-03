strg=input()
count=0
for i in range(len(strg)):
  if(strg[i].isdigit() or strg[i].isalpha() or strg[i]==(" ")):
    continue
  else:
    count+=1
print(count)
