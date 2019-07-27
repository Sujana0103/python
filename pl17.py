a1,b2 = input().split()
b2 = int(b2)
fake = False
l = list(map(int,input().split()))
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j] == b2:
            fake = True
print("yes" if fake else "no") 
