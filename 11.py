number,exponent=map(int,input().split())
power=1
for i in range(1,exponent+1):
  power=power*number
print(power)
