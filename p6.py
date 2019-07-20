a1,b2=map(str,input().split())
for i in range(len(a1)):
    if(a1.count(a1[i])==b2.count(b2[i])):
        print("yes")
        break
    else:
        print("no")
        break
