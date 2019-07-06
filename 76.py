intg=int(input())
if(intg>1):
 for i in range(2,intg):
  if(intg%i==0):
   print("yes")
   break
 else:
   print("no")
